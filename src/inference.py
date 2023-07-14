import os
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings


os.environ["OPENAI_API_KEY"] = ""


def process_data(
    path_pdf: str "",
    is_local: bool = False
):
    _, loader = os.system('curl -o %s %s' % (default_name, path_pdf), PyPDFLoader(default_name))
    
    
    
doc = loader.load_document()

doc = loader.load_and_split()
embeddings = OpenAIEmbeddings()
 db = Chroma.from_documents(doc, emnedding = embeddings)
 
 qa = RetriveQa.from_documents(llm= )


embeddings_model = OpenAIEmbeddings(OPENAI_API_KEY)