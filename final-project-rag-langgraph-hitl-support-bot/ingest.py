from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

def create_vector_db(pdf_path):

    print("📄 Loading PDF...")

    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    # SAFE CHUNKING
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(docs)

    print(f"✅ Created {len(chunks)} chunks")

    # EMBEDDINGS
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # VECTOR DB
    db = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory="./chroma_db"
    )

    print("✅ Vector DB ready")

    return db
