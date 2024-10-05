from pdf_processing import extract_text_from_pdf
from qa_system import create_pdf_qa_system
from chat_ui import chat_ui

def main():
    # PDF 파일 경로
    pdf_text = extract_text_from_pdf("pdfs\test_sample.pdf")
    
    # PDF 내용을 기반으로 한 QA 시스템 생성
    qa_system = create_pdf_qa_system(pdf_text)
    
    # Streamlit UI 실행
    chat_ui(qa_system)

if __name__ == "__main__":
    main()
