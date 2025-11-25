from langchain_experimental.text_splitter import SemanticChunker
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_openai.embeddings.base import OpenAIEmbeddings

splitter = SemanticChunker(
    OllamaEmbeddings(model="llama3.2"), breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=2
)

text = """
Pune, often called the "Oxford of the East," is a vibrant Indian city known for its rich cultural heritage, educational institutions, pleasant weather, and rapidly growing IT sector. It blends traditional Maharashtrian culture with modern urban development, making it a major hub for students, professionals, and startups. In recent years, Pune has also seen increased interest in AI technologies, including LangChain, a powerful framework for building applications using large language models. LangChain simplifies the process of creating chatbots, autonomous agents, retrieval systems, and workflow automation by offering modular tools and integrations that help developers build scalable, production-ready LLM applications.

MCP servers, short for Model Context Protocol servers, provide a structured way for applications to expose capabilities, data, and tools that large language models can use. They act as a bridge between an LLM and external systems, enabling dynamic interactions such as executing tools, fetching resources, or performing actions requested by a client. MCP servers support predictable, schema-driven communication, making them reliable for automation workflows, agent-based systems, and complex integrations. By defining tools, resources, and metadata clearly, MCP servers ensure consistent behavior across environments. This architecture improves flexibility, security, and maintainability when developing advanced AI-driven applications that rely on external services.
"""
docs = splitter.create_documents([text])
print(len(docs))
print(docs)
