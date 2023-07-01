import io
import pypdf


def summary(pdf_file, page_number):
    return pdf_file.pages[page_number].extract_text()

def get_pdf(file_object):
    return pypdf.PdfReader(io.BytesIO(file_object))
