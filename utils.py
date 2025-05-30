import fitz  # PyMuPDF

def read_pdf_text(pdf_path):
    """
    Extracts and returns text from a PDF file using PyMuPDF.
    
    Args:
        pdf_path (str): Path to the PDF file.
    
    Returns:
        str: Combined text from all pages.
    """
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            text += page.get_text()
        doc.close()
    except Exception as e:
        print(f"[ERROR] Failed to read PDF: {e}")
    return text.strip()
