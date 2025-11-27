from langchain_community.document_loaders import PyPDFLoader



loader = PyPDFLoader('jmeter_beginner_friendly_manual.pdf')

docs = loader.load()

print(docs)
print(len(docs))
print(docs)
# print(docs[0].page_content)
# print(docs[0].metadata)