import subprocess
import sys

try:
  import pdfplumber
except ImportError:
  subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pdfplumber'])
  import pdfplumber

try:
  import psutil
except ImportError:
  subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'psutil'])
  import psutil

def check_mem(thresh=0.9):
  return psutil.virtual_memory().percent >= thresh * 100

def pdf_to_text(pdf_file, txt_file, start_page=0):

  with open(txt_file, 'a', encoding='utf-8') as out:

    pdf = pdfplumber.open(pdf_file)
    total_pages = len(pdf.pages)

    for i in range(start_page, total_pages):
    
      if check_mem():
        print("Memory exceeded 90%, stopping.")
        return i

      page = pdf.pages[i]
      text = page.extract_text()
      out.write(text + '\n')
      print(f"\rPages Done: {i+1}/{total_pages}", end='')

    return total_pages

if __name__ == "__main__":

  pdf_file = input("Enter PDF file: ")
  txt_file = input("Enter TXT file: ")

  pdf = pdfplumber.open(pdf_file)
  total_pages = len(pdf.pages)
  
  current_page = 0

  while current_page < total_pages:
    current_page = pdf_to_text(pdf_file, txt_file, start_page=current_page)

  print("\nText extraction complete!")