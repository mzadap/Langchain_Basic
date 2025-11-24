from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='resources',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.load()

for document in docs:
    print(document.metadata)

#lazy load
#docs = loader.lazy_load()