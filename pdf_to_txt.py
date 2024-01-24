# -*- coding: utf-8 -*-
# importing required modules
try:
    import PyPDF2
except ImportError:
    import os
    os.system('pip install PyPDF2')
    import PyPDF2

def extract_text_from_pdf(pdf_filename, txt_filename):
    # creating a pdf reader object 
    reader = PyPDF2.PdfReader(pdf_filename) 

    # printing number of pages in pdf file 
    print(len(reader.pages)) 

    # extracting text from all pages and saving to txt file
    with open(txt_filename, 'w', encoding='utf-8') as f:  # Open the file with UTF-8 encoding
        for page in reader.pages:
            text = page.extract_text() 
            f.write(text + '\n')

if __name__ == "__main__":
    pdf_filename = input("Please enter the path to the PDF file: ")
    txt_filename = input("Please enter the path to the output text file: ")

    if not pdf_filename.endswith(".pdf"): #check pdf file
        print("No pdf file specified")
    elif not txt_filename.endswith(".txt"): #check txt file
        print("No txt file specified")
    else:
        # Migrating starts here....
        extract_text_from_pdf(pdf_filename, txt_filename)


