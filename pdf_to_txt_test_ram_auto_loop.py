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

try:
    import psutil
except ImportError:
    install('psutil')
    import psutil

def check_memory_usage(threshold=0.9):
    mem = psutil.virtual_memory()
    return mem.percent >= threshold * 100

def extract_text_from_pdf_with_pdfplumber(pdf_filename, txt_filename):
    start_page = 0
    while True:
        with pdfplumber.open(pdf_filename) as pdf:
            total_pages = len(pdf.pages)
            print(f"Total pages in the PDF: {total_pages}")
        
            with open(txt_filename, 'a', encoding='utf-8') as f:
                for i in range(start_page, total_pages):
                    if check_memory_usage():
                        print("Memory usage exceeded 90%, stopping conversion.")
                        start_page = i
                        break
                    text = pdf.pages[i].extract_text()
                    f.write(text + '\n')
                    print(f"Total pages converted: {i+1}", end="\r")
                else:
                    break

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