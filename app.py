from flask import Flask
import pdfplumber

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/file')
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

text = extract_text_from_pdf("Cox and Kings Ltd vs SAP India Pvt. Ltd. & Anr.pdf")
print(text)
