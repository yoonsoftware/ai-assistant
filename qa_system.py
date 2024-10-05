from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

def create_pdf_qa_system(pdf_text):
    """PDF 텍스트 기반의 질문-답변 시스템을 생성하는 함수"""
    embeddings = OpenAIEmbeddings()
    vector_store = Chroma.from_texts([pdf_text], embeddings)
    llm = OpenAI()
    qa_chain = RetrievalQA(llm=llm, retriever=vector_store.as_retriever())
    return qa_chain
