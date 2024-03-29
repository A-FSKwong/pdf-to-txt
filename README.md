# pdf-to-txt
Converts pdf file to txt file , run in cmd and user can input the path of input and output file.
The codes was originally from the project of "wwiras/mypdf2text". Thank you very much for wwiras's great codes.

I modified his code to be able to run in CMD with user input prompt, and could convert code in "UTF-8" rather than
wwiras's "cp1252", using UTF-8 encoding, supports a wider range of characters, especially when handling Chinese. 


在程式碼中加入一個迴圈，讓程式在記憶體使用量超過 90% 並停止轉換後，能夠自動重新開始轉換。以下是修改後的程式碼：

```python
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
```

這段程式碼會在每次處理一頁 PDF 文件之前，檢查系統的記憶體使用情況。如果記憶體使用量超過了 90%，程式就會停止轉換，並記錄下停止的頁面。
然後，程式會自動重新開始轉換，從停止的頁面開始，並將轉換的內容追加到輸出的文字檔案中。這個過程會一直重複，直到所有的 PDF 頁面都被轉換完畢。


