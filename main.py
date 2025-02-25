import os
import glob

print(os.path.exists(r'C:\Users\Dominik\Downloads'))
pdf_files = glob.glob("C:/Users/Dominik/Downloads/*.pdf")
for pdf in pdf_files:
    print(pdf)