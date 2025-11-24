from langchain_community.document_loaders import WebBaseLoader
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


model = ChatOllama(model="llama3.2")

prompt = PromptTemplate(
    template = 'Answer the following questions \n {question} from the following text -  \n {text} ',
    input_variables = ['question', 'text']
)
parser = StrOutputParser()
url = "https://www.flipkart.com/apple-watch-ultra-3-gps-cellular-49mm-black-titanium-case-alpine-loop-large/p/itme78e8c3ae379b"

loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

print(chain.invoke({
    'question' : 'can you me xpath for Add to cart button',
    'text': docs[0].page_content
}))