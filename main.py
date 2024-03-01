import pytesseract
from PIL import Image

from docx import Document
import docx

import textract

from pdf2image import convert_from_path

import os
import sys

import spacy
from spacy.tokens import DocBin
from tqdm import tqdm
import json

# remove warnings
import warnings
warnings.filterwarnings("ignore")


# Configuration
pytesseract.pytesseract.tesseract_cmd = r'./tools/Tesseract-OCR/tesseract.exe'


# extract text from file

def txt_to_text(path_to_file):
    # Open the file in read mode
    with open(path_to_file, 'r') as file:
        # Read the contents of the file
        resume_text = file.read()
    return resume_text

def image_to_text(path_to_file):
    # Open the image using PIL (Python Imaging Library)
    image = Image.open(path_to_file)
    # Perform OCR using pytesseract
    text = pytesseract.image_to_string(image)

    return text

def pdf_to_text(path_to_file):
    # Convert each page of the PDF to images
    pages = convert_from_path(path_to_file, dpi=300, poppler_path=r"./tools/poppler-24.02.0/Library/bin/")

    text_data = ''
    for page in pages:
        text = pytesseract.image_to_string(page)
        text_data += text + '\n'
        
    return text_data

def docx_to_text(path_to_file):
    doc = Document(path_to_file)
    text_content = ''

    for paragraph in doc.paragraphs:
        text_content += paragraph.text + '\n'

    return text_content

def html_to_text(path_to_file):
    text_content = textract.process(path_to_file).decode('utf-8')
    return text_content


# Get text from given file type

def get_text_from_file(path_to_file):
    if not os.path.exists(path_to_file):
        return "File not found"

    file_name, file_extension = os.path.splitext(path_to_file)
    file_extension = file_extension.lower()

    if file_extension == ".txt":
        return txt_to_text(path_to_file)
    
    elif file_extension in (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"):
        return image_to_text(path_to_file)
    
    elif file_extension == ".pdf":
        return pdf_to_text(path_to_file)
    elif file_extension == ".docx":
        return docx_to_text(path_to_file)
    elif file_extension in (".html", ".htm"):
        return html_to_text(path_to_file)
    else:
        return "Unknown file type"
    

if __name__ == "__main__":
    
    if(len(sys.argv) <= 1 or len(sys.argv) > 2):
        print('Usage: python main.py <inputfile>')
    else: 
        file_path = sys.argv[1]
        
        #  Get text of files
        text = get_text_from_file(file_path)
        
        if(text == "File not found"):
            print("File not found!")
            
        elif(text == "Unknown file type"):
            print("File should be only in txt, image, pdf, docx, html and htm format.\n")

        else:
            print('Processing your document...\n')
            try:
                # load model
                nlp=spacy.load("./model-best")
                
                # get entities from text
                doc=nlp(text)
                
                res = dict()
                
                for ent in doc.ents:
                    res[ent.label_] = []
                    # print(ent.text,"->>", ent.label_)
                    
                for ent in doc.ents:
                    res[ent.label_].append(ent.text)
                    
                print(res)
                
            except Exception as e:
                print("Something went wrong! Please try again...")
        
        

