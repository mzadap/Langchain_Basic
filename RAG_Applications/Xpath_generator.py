from langchain_community.document_loaders import SeleniumURLLoader
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama



# STEP 1 — Load webpage HTML using SeleniumURLLoader
def load_html(url: str) -> str:
    loader = SeleniumURLLoader(urls=[url])
    docs = loader.load()
    html = docs[0].page_content
    
    # Limit HTML size if too large (to avoid token limits)
    max_chars = 100000  # ~25k tokens roughly
    if len(html) > max_chars:
        print(f"⚠️  HTML too large ({len(html)} chars), truncating to {max_chars}...")
        html = html[:max_chars]
    
    return html


# STEP 2 — Generate XPath using LLM
def generate_xpath(html: str, query: str) -> str:
    template = """
You are an XPath expert. Your job is to return ONLY a valid XPath expression, nothing else.

Task: Find the element described as: "{query}"

HTML snippet:
{html}

CRITICAL RULES:
- Return ONLY the XPath string (e.g., //input[@name='q'])
- NO code blocks, NO explanations, NO markdown
- NO Python code, NO selenium code
- JUST the XPath expression
- Start with // or /

Your response:"""

    prompt = PromptTemplate(
        input_variables=["html", "query"], template=template
    )

    llm = ChatOllama(
        model="llama3.2",
        temperature=0  # More deterministic output
    )

    chain = prompt | llm
    response = chain.invoke({"html": html, "query": query})

    # Clean up the response
    xpath = response.content.strip()
    
    # Remove markdown code blocks if present
    if "```" in xpath:
        xpath = xpath.split("```")[1] if len(xpath.split("```")) > 1 else xpath
        xpath = xpath.replace("xpath", "").replace("python", "").strip()
    
    # Remove quotes if present
    xpath = xpath.strip('"').strip("'")
    
    # Get first line only
    xpath = xpath.split("\n")[0].strip()
    
    return xpath


# STEP 3 — Validate XPath using Selenium Browser
def validate_xpath(url: str, xpath: str):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import NoSuchElementException
    from selenium.webdriver.chrome.options import Options
    
    # Setup headless Chrome for faster execution
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        driver.implicitly_wait(5)  # Wait for page load
        
        try:
            element = driver.find_element(By.XPATH, xpath)
            print("✅ XPath is VALID")
            
            # Show element details
            tag = element.tag_name
            text = element.text[:100] if element.text else "(no text)"
            print(f"   Tag: <{tag}>")
            print(f"   Text: {text}")
            
            driver.quit()
            return True
        
        except NoSuchElementException:
            print("❌ XPath INVALID - Element not found")
            driver.quit()
            return False
            
    except Exception as e:
        print(f"❌ Validation error: {str(e)}")
        return False


# MAIN FUNCTION
def smart_xpath(url: str, user_query: str):
    print("\n🔄 Loading page...")
    html = load_html(url)

    print("\n🤖 Generating XPath...")
    xpath = generate_xpath(html, user_query)
    print("\n📌 Suggested XPath:", xpath)

    print("\n🔍 Validating...")
    is_valid = validate_xpath(url, xpath)

    return xpath if is_valid else None



smart_xpath(
    url="https://practicetestautomation.com/practice-test-login/",
    user_query="Submit button"
)
