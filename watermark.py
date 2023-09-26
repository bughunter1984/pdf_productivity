# Please adapt the file names to your own needs
import PyPDF2

input_file = PyPDF2.PdfReader(open("super.pdf", "rb"))
watermark_pdf = PyPDF2.PdfReader(open("wtr.pdf", "rb"))
output = PyPDF2.PdfWriter()

for i in range(len(input_file.pages)):
    pdf_page = input_file.pages[i]
    pdf_page.merge_page(watermark_pdf.pages[0])
    output.add_page(pdf_page)

with open("wtr_file.pdf", "wb") as merged_file:
    output.write(merged_file)
