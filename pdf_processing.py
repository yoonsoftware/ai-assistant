import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """PDF 파일에서 텍스트를 추출하는 함수"""
    with fitz.open(pdf_path) as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    return text
