

from langchain_community.document_loaders import WebBaseLoader, AsyncHtmlLoader, SeleniumURLLoader
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


model = ChatOllama(model="llama3.2")

prompt = PromptTemplate(
    template = """
You are an expert in Selenium and XPath creation.
User wants to locate an element based on this description: "{query}"

Below is the webpage HTML: {html}

Return ONLY the best possible XPath selector.
Do NOT include explanation.
""",
    input_variables = ['query', 'html']
)
parser = StrOutputParser()


url = ["https://www.flipkart.com"]
loader = SeleniumURLLoader(url)

docs = loader.load()
#print(docs[0].page_content)

chain = prompt | model

response =  chain.invoke({
    'query' : 'the search input box',
    'html': docs[0].page_content
})
print(response.content.strip())

