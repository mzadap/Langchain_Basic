import ssl

from langchain_community.document_loaders import WebBaseLoader, AsyncHtmlLoader, SeleniumURLLoader
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


model = ChatOllama(model="llama3.2")

prompt = PromptTemplate(
    template = """
You are an expert in Selenium and XPath creation.
User wants to locate an element based on this description:

Description: {question}

Below is the webpage HTML:

{text}

Return ONLY the best possible XPath selector.
Do NOT include explanation.
""",
    input_variables = ['question', 'text']
)
parser = StrOutputParser()


url = ["https://www.flipkart.com"]
loader = SeleniumURLLoader(url)

docs = loader.load()
#print(docs[0].page_content)

chain = prompt | model | parser

print(chain.invoke({
    'question' : 'xpath for become a seller link',
    'text': docs[0].page_content
}))