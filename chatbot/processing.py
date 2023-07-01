import io
import pypdf
import langchain
from langchain.docstore.document import Document
from langchain import OpenAI, PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from dotenv import load_dotenv


def get_summary(pdf_file, page_number):
    load_dotenv()
    page = Document(page_content=pdf_file.pages[page_number].extract_text(), page_number=page_number)
    llm = OpenAI(temperature=0)
    prompt_template = "Write a short summary of the following: {text} START SUMMARY WITH -'THIS PAGE':"
    PROMPT = PromptTemplate(template=prompt_template, input_variables=["text"])
    chain = load_summarize_chain(llm, chain_type="stuff", prompt=PROMPT)
    return chain.run([page])

def get_pdf(file_object):
    return pypdf.PdfReader(io.BytesIO(file_object))
