from click import prompt
from langchain_community.document_loaders import TextLoader
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(model="llama3.2")

prompt = PromptTemplate(
    template = 'Write Types of Performance Testing With JMeter the following document \n {jmeter} ',
    input_variables = ['jmeter']
)

parser = StrOutputParser()

loader = TextLoader('jmeter_performance_testing.txt', encoding='utf-8')

docs = loader.load()

# print(docs)
# print(docs[0].page_content)

# print(docs)
#
# print(type(docs))
#
# print(len(docs))

chain = prompt | model | parser

print(chain.invoke({'jmeter': docs[0].page_content}))

