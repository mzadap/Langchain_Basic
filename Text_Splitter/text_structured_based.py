from langchain.text_splitter import RecursiveCharacterTextSplitter


text = """
LangChain is a powerful framework designed to build applications that integrate large language models with external data, tools, and workflows. It simplifies tasks like document loading, text processing, building conversational agents, and creating custom pipelines using LLMs. With its modular components—such as loaders, embeddings, vector stores, and chains—LangChain enables developers to create intelligent applications that can reason, retrieve, and respond more effectively. It supports multiple models and integrations, making it flexible for real-world use cases like chatbots, RAG systems, automation, and analytics. Overall, LangChain helps developers streamline LLM-based development with a structured, scalable approach.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0
)

result = splitter.split_text(text)
print(len(result))
print(result)