from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from sympy.printing.tree import print_node

loader = DirectoryLoader(
    path='resources',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

#docs = loader.load()

#print(docs)

# for document in docs:
#     print(document.page_content)

#lazy load
docs = loader.lazy_load()
for document in docs:
    print(document.page_content)