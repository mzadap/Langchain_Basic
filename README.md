# Langchain Learning Project

A comprehensive collection of Langchain examples and implementations covering RAG (Retrieval-Augmented Generation) applications and structured outputs with LLMs.

## 📋 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Modules](#modules)
  - [RAG Applications](#rag-applications)
  - [Structured Outputs](#structured-outputs)
- [Usage Examples](#usage-examples)
- [Requirements](#requirements)

## Overview

This project demonstrates various Langchain capabilities including:
- **Document Loading**: Multiple loaders for different data formats (PDF, CSV, Text, Web)
- **RAG Applications**: Implementing Retrieval-Augmented Generation workflows
- **Structured Outputs**: Using Pydantic and TypedDict for structured LLM responses

## Project Structure

```
Langchain/
├── RAG_Applications/
│   ├── csv_loader.py           # Load and process CSV files
│   ├── pdf_loader.py            # Load and process PDF documents
│   ├── text_loader.py           # Load and process text files
│   ├── webbase_loader.py        # Load content from web URLs
│   ├── directory_loader.py      # Load multiple files from directories
│   ├── resources/               # Sample data files
│   │   ├── csv/
│   │   │   └── AI_DataScience_90Day_Roadmap_Notion.csv
│   │   ├── Gatling User Guide.pdf
│   │   ├── MCP evaluations or MCP testing.pdf
│   │   └── Python+Handbook.pdf
│   ├── jmeter_beginner_friendly_manual.pdf
│   └── jmeter_performance_testing.txt
│
└── Structured_outputs/
    ├── Pydentic_Demo.py                          # Basic Pydantic usage
    ├── with_structured_output_pydantic.py        # Structured outputs with Pydantic
    ├── with_structured_output_pydantic_json.py   # JSON-based structured outputs
    ├── with_Structured_output_typeddict.py       # TypedDict implementation
    ├── TypeDict.py                               # TypedDict examples
    └── json_schema.json                          # JSON schema definitions
```

## Installation

### Prerequisites

- Python 3.8+
- pip package manager

### Setup

1. Clone or navigate to the project directory:
```bash
cd /path/to/Langchain
```

2. Install required dependencies:
```bash
pip install langchain langchain-community langchain-ollama pydantic pypdf
```

3. (Optional) If using Ollama models, install Ollama:
```bash
# Visit https://ollama.ai for installation instructions
# Pull required models
ollama pull llama3.2
```

## Modules

### RAG Applications

The `RAG_Applications` directory contains various document loaders for building RAG pipelines:

#### CSV Loader (`csv_loader.py`)
- Loads CSV files using `CSVLoader`
- Processes tabular data for RAG applications
- Example: AI & Data Science roadmap data

#### PDF Loader (`pdf_loader.py`)
- Loads PDF documents using `PyPDFLoader`
- Extracts text content and metadata
- Supports multi-page PDFs

#### Text Loader (`text_loader.py`)
- Loads plain text files
- Processes unstructured text data

#### Web Loader (`webbase_loader.py`)
- Fetches and loads content from web URLs
- Useful for dynamic content retrieval

#### Directory Loader (`directory_loader.py`)
- Batch loads multiple files from a directory
- Supports various file formats

### Structured Outputs

The `Structured_outputs` directory demonstrates how to get structured responses from LLMs:

#### Pydantic Models (`with_structured_output_pydantic.py`)
- Uses Pydantic `BaseModel` for schema definition
- Field validation and descriptions
- Example: Product review analysis with sentiment, themes, pros/cons
- Compatible with `ChatOllama` and other LLM providers

#### TypedDict (`with_Structured_output_typeddict.py`)
- Alternative approach using Python's `TypedDict`
- Lighter weight than Pydantic
- Type hints for structured data

#### Pydantic Demo (`Pydentic_Demo.py`)
- Basic Pydantic usage examples
- Field constraints and validation
- Model serialization

## Usage Examples

### Loading a PDF Document

```python
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('path/to/document.pdf')
docs = loader.load()

print(f"Loaded {len(docs)} pages")
print(docs[0].page_content)  # First page content
print(docs[0].metadata)       # Document metadata
```

### Loading CSV Data

```python
from langchain_community.document_loaders import CSVLoader

loader = CSVLoader("path/to/data.csv")
docs = loader.load()

for document in docs:
    print(document.page_content)
```

### Structured Output with Pydantic

```python
from langchain_ollama import ChatOllama
from pydantic import BaseModel, Field
from typing import Literal, Optional

class Review(BaseModel):
    key_theme: list[str] = Field(description='Key themes in the review')
    summary: str = Field(description='Brief summary')
    sentiment: Literal['positive', 'negative', 'neutral']
    pros: Optional[list[str]] = Field(default=None)
    cons: Optional[list[str]] = Field(default=None)

model = ChatOllama(model="llama3.2")
structured_model = model.with_structured_output(Review)

result = structured_model.invoke("Your review text here...")
print(result.key_theme)
print(result.summary)
```

## Requirements

Core dependencies:
- `langchain` - Main Langchain library
- `langchain-community` - Community integrations
- `langchain-ollama` - Ollama integration
- `pydantic` - Data validation and schema definition
- `pypdf` - PDF processing

## Resources

Sample files included in the project:
- JMeter performance testing documentation
- Gatling user guide
- Python handbook
- AI & Data Science roadmap (CSV)
- MCP evaluation documentation

## Learning Path

1. **Start with RAG Applications**: Learn document loading basics
2. **Explore Document Loaders**: Try different formats (PDF, CSV, Text, Web)
3. **Understand Structured Outputs**: Move to Pydantic examples
4. **Build Complex Schemas**: Create custom models for your use cases
5. **Combine Both**: Build RAG applications with structured outputs

## Notes

- The project uses `ChatOllama` with the `llama3.2` model for structured outputs
- All document loaders are from `langchain_community`
- Structured output examples demonstrate real-world use cases like review analysis

## License

This is a learning project for educational purposes.

---

Happy Learning! 🚀

