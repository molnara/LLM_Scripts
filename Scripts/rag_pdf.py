from langchain_community.document_loaders import PyPDFLoader # type: ignore

file_path = "./example_data/nke-10k-2023.pdf"
loader = PyPDFLoader(file_path)

docs = loader.load()

from langchain_ollama import ChatOllama # type: ignore

model = ChatOllama(
    model="deepseek-r1",
)

from langchain_text_splitters import RecursiveCharacterTextSplitter # type: ignore

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
all_splits = text_splitter.split_documents(docs)

__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

from langchain_chroma import Chroma # type: ignore
from langchain_ollama import OllamaEmbeddings # type: ignore

local_embeddings = OllamaEmbeddings(model="nomic-embed-text")

vectorstore = Chroma.from_documents(documents=all_splits, embedding=local_embeddings)

retriever = vectorstore.as_retriever()

from langchain.chains import create_retrieval_chain # type: ignore
from langchain.chains.combine_documents import create_stuff_documents_chain # type: ignore
from langchain_core.prompts import ChatPromptTemplate # type: ignore

system_prompt = (
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer "
    "the question. If you don't know the answer, say that you "
    "don't know. Use three sentences maximum and keep the "
    "answer concise."
    "\n\n"
    "{context}"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)


question_answer_chain = create_stuff_documents_chain(model, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

results = rag_chain.invoke({"input": "What was Nike's revenue in 2023?"})

print(results["context"][0].page_content)

print(results["context"][0].metadata)
