from langchain.document_loaders.pdf import PyPDFDirectoryLoader

DATA_PATH = "."
def load_documents():
    document_loader = PyPDFDirectoryLoader(DATA_PATH)
    return document_loader.load()

documents = load_documents()
print(documents)

