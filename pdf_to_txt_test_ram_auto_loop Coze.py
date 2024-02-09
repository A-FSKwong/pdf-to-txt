import subprocess
import sys

# Define a function to install required packages
def install_packages(packages):
    subprocess.check_call([sys.executable, "-m", "pip", "install"] + packages)

# Install the required packages at the start if they are not already installed
required_packages = ['pdfplumber', 'psutil']
install_packages(required_packages)

import pdfplumber
import psutil

# Function to check memory usage
def check_memory_usage(threshold=0.9):
    mem = psutil.virtual_memory()
    return mem.percent >= threshold * 100

# Function to extract text from PDF using pdfplumber
def extract_text_from_pdf_with_pdfplumber(pdf_filename, txt_filename):
    with pdfplumber.open(pdf_filename) as pdf:
        total_pages = len(pdf.pages)
        print(f"Total pages in the PDF: {total_pages}")

        with open(txt_filename, 'w', encoding='utf-8') as f:
            for i, page in enumerate(pdf.pages):
                if i % 10 == 0 and check_memory_usage():  # Check memory usage every 10 pages
                    print(f"Memory usage exceeded 90% after processing {i} pages, stopping conversion.")
                    break
                text = page.extract_text()
                if text:
                    f.write(text + '\n')
                sys.stdout.write(f"\rTotal pages converted: {i+1}")
                sys.stdout.flush()

if __name__ == "__main__":
    pdf_filename = input("Please enter the path to the PDF file: ")
    txt_filename = input("Please enter the path to the output text file: ")

    if not pdf_filename.endswith(".pdf"):
        print("No pdf file specified")
    elif not txt_filename.endswith(".txt"):
        print("No txt file specified")
    else:
        print("Extracting text with pdfplumber...")
        extract_text_from_pdf_with_pdfplumber(pdf_filename, txt_filename)

    print("\nAll Done.")