# -*- coding: utf-8 -*-
# importing required modules
import os
import sys
import subprocess

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

try:
    import pdfplumber
except ImportError:
    install('pdfplumber')
    import pdfplumber


def extract_text_from_pdf_with_pdfplumber(pdf_filename, txt_filename):
    with pdfplumber.open(pdf_filename) as pdf:
        total_pages = len(pdf.pages)
        print(f"Total pages in the PDF: {total_pages}")
    
        with open(txt_filename, 'w', encoding='utf-8') as f:
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                f.write(text + '\n')
                print(f"Total pages converted: {i+1}", end="\r")


if __name__ == "__main__":
    pdf_filename = input("Please enter the path to the PDF file: ")
    txt_filename = input("Please enter the path to the output text file: ")

    if not pdf_filename.endswith(".pdf"): #check pdf file
        print("No pdf file specified")
    elif not txt_filename.endswith(".txt"): #check txt file
        print("No txt file specified")
    else:
        # Migrating starts here....
        print("Extracting text with pdfplumber...")
        extract_text_from_pdf_with_pdfplumber(pdf_filename, txt_filename)

    print("\nAll Done.")