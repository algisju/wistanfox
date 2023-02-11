import os
import pandas as pd
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import codecs

def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    fake_file_handle = StringIO()
    converter = TextConverter(resource_manager, fake_file_handle,laparams=LAParams())
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
 
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, 
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)
        text = fake_file_handle.getvalue()
 
    # close open handles
    converter.close()
    fake_file_handle.close()
 
    if text:
        return text


def create_text_files(directory):
    pdf_files = [f for f in os.listdir(directory) if f.endswith('.pdf')]
    for pdf_file in pdf_files:
        pdf_path = os.path.join(directory, pdf_file)
        text = extract_text_from_pdf(pdf_path)
        text_file_path = os.path.splitext(pdf_path)[0] + '.txt'
        with open(text_file_path, 'w', encoding='utf-8') as f:
            f.write(text)

def create_dataset(directory):
    pdf_files = [f for f in os.listdir(directory) if f.endswith('.pdf')]
    pdf_texts = [extract_text_from_pdf(os.path.join(directory, pdf_file)) for pdf_file in pdf_files]
    df = pd.DataFrame({'file_name': pdf_files, 'text': pdf_texts})
    return df


codec='utf-8'
directory = './pdf'
create_text_files(directory)
df = create_dataset(directory)
print(df)