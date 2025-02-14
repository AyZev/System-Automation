import os
from PyPDF2 import PdfReader, PdfWriter

def path(pdf_name):
    return fr"C:/Users/YourUsername/Downloads/Documents/{pdf_name}"

pdf_name = path('oldpdfname.pdf')

print(os.path.exists(pdf_name))

reader = PdfReader(pdf_name)
reader.decrypt("password")

writer = PdfWriter()
for page in reader.pages :
    writer.add_page(page)
    
with open('path','wb') as f:
    writer.write(f)
    
new_pdf_name = path('newpdfname.pdf')

with open(new_pdf_name, 'wb') as f:
    writer.write(f)
    
os.remove(pdf_name)