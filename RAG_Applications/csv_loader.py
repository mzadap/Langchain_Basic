from langchain_community.document_loaders import CSVLoader


loader = CSVLoader("resources/csv/AI_DataScience_90Day_Roadmap_Notion.csv")

docs = loader.load()

print(docs)
print(docs[0].page_content)

for document in docs:
    print(document.page_content)