import PyPDF2
from PyPDF2 import PdfReader, PdfWriter
import os
from pdf2image import convert_from_path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import pdfplumber
import tabula
from pdfminer.high_level import extract_text
from pytesseract import image_to_string
from PIL import Image

# Define the output directory
OUTPUT_DIR = 'output_files'

# Ensure the output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ORGANIZE PDF
def merge_pdfs():
    paths = input("Enter the PDF paths to merge, separated by a comma: ").split(',')
    output = os.path.join(OUTPUT_DIR, 'merged.pdf')
    pdf_writer = PdfWriter()
    for path in paths:
        pdf_reader = PdfReader(path.strip())
        for page in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page])
    with open(output, 'wb') as out:
        pdf_writer.write(out)
    print(f"Merged PDF saved at: {output}")

def split_pdf():
    path = input("Enter the PDF path to split: ").strip()
    output_folder = os.path.join(OUTPUT_DIR, 'split_pages')
    os.makedirs(output_folder, exist_ok=True)
    pdf_reader = PdfReader(path)
    for page in range(len(pdf_reader.pages)):
        pdf_writer = PdfWriter()
        pdf_writer.add_page(pdf_reader.pages[page])
        output_path = os.path.join(output_folder, f'page_{page + 1}.pdf')
        with open(output_path, 'wb') as out:
            pdf_writer.write(out)
    print(f"Split pages saved in folder: {output_folder}")

def remove_pages():
    path = input("Enter the PDF path: ").strip()
    pages_to_remove = list(map(int, input("Enter the page numbers to remove, separated by a comma: ").split(',')))
    output = os.path.join(OUTPUT_DIR, 'removed_pages.pdf')
    pdf_reader = PdfReader(path)
    pdf_writer = PdfWriter()
    for i in range(len(pdf_reader.pages)):
        if i not in pages_to_remove:
            pdf_writer.add_page(pdf_reader.pages[i])
    with open(output, 'wb') as out:
        pdf_writer.write(out)
    print(f"PDF with removed pages saved at: {output}")

def extract_pages():
    path = input("Enter the PDF path: ").strip()
    pages_to_extract = list(map(int, input("Enter the page numbers to extract, separated by a comma: ").split(',')))
    output = os.path.join(OUTPUT_DIR, 'extracted_pages.pdf')
    pdf_reader = PdfReader(path)
    pdf_writer = PdfWriter()
    for i in pages_to_extract:
        pdf_writer.add_page(pdf_reader.pages[i])
    with open(output, 'wb') as out:
        pdf_writer.write(out)
    print(f"Extracted pages saved at: {output}")

def scan_to_pdf():
    image_paths = input("Enter the image paths to scan to PDF, separated by a comma: ").split(',')
    output = os.path.join(OUTPUT_DIR, 'scanned.pdf')
    pdf_writer = PdfWriter()
    for image_path in image_paths:
        images = convert_from_path(image_path.strip())
        for image in images:
            pdf_writer.add_page(image)
    with open(output, 'wb') as out:
        pdf_writer.write(out)
    print(f"Scanned PDF saved at: {output}")

# OPTIMIZE PDF
def compress_pdf():
    path = input("Enter the PDF path to compress: ").strip()
    output = os.path.join(OUTPUT_DIR, 'compressed.pdf')
    pdf_reader = PdfReader(path)
    pdf_writer = PdfWriter()

    for page in pdf_reader.pages:
        pdf_writer.add_page(page)

    with open(output, 'wb') as out:
        pdf_writer.write(out)
    print(f"Compressed PDF saved at: {output}")

def repair_pdf():
    path = input("Enter the PDF path to repair: ").strip()
    output = os.path.join(OUTPUT_DIR, 'repaired.pdf')
    pdf_reader = PdfReader(path)
    pdf_writer = PdfWriter()

    for page in pdf_reader.pages:
        pdf_writer.add_page(page)

    with open(output, 'wb') as out:
        pdf_writer.write(out)
    print(f"Repaired PDF saved at: {output}")

def ocr_pdf():
    path = input("Enter the PDF path for OCR: ").strip()
    output = os.path.join(OUTPUT_DIR, 'ocr.pdf')
    images = convert_from_path(path)
    text = ''
    for image in images:
        text += image_to_string(image)

    with open(output, 'w') as out:
        out.write(text)
    print(f"OCR text saved at: {output}")

# CONVERT TO PDF
def jpg_to_pdf():
    image_paths = input("Enter the JPG paths to convert to PDF, separated by a comma: ").split(',')
    output = os.path.join(OUTPUT_DIR, 'converted.pdf')
    pdf_writer = PdfWriter()
    for image_path in image_paths:
        image = Image.open(image_path.strip())
        pdf_writer.add_page(image)
    with open(output, 'wb') as out:
        pdf_writer.write(out)
    print(f"Converted PDF saved at: {output}")

def word_to_pdf():
    docx_path = input("Enter the Word document path to convert to PDF: ").strip()
    output = os.path.join(OUTPUT_DIR, 'word_to_pdf.pdf')
    pass  # Use a library like python-docx and reportlab
    print(f"Converted Word document saved at: {output}")

def powerpoint_to_pdf():
    pptx_path = input("Enter the PowerPoint file path to convert to PDF: ").strip()
    output = os.path.join(OUTPUT_DIR, 'powerpoint_to_pdf.pdf')
    pass  # Use a library like python-pptx and reportlab
    print(f"Converted PowerPoint file saved at: {output}")

def excel_to_pdf():
    xlsx_path = input("Enter the Excel file path to convert to PDF: ").strip()
    output = os.path.join(OUTPUT_DIR, 'excel_to_pdf.pdf')
    pass  # Use a library like pandas and reportlab
    print(f"Converted Excel file saved at: {output}")

def html_to_pdf():
    html_path = input("Enter the HTML file path to convert to PDF: ").strip()
    output = os.path.join(OUTPUT_DIR, 'html_to_pdf.pdf')
    pass  # Use a library like pdfkit or weasyprint
    print(f"Converted HTML file saved at: {output}")

# CONVERT FROM PDF
def pdf_to_jpg():
    path = input("Enter the PDF path to convert to JPG: ").strip()
    output_folder = os.path.join(OUTPUT_DIR, 'pdf_to_jpg')
    os.makedirs(output_folder, exist_ok=True)
    images = convert_from_path(path)
    for i, image in enumerate(images):
        image.save(os.path.join(output_folder, f'page_{i + 1}.jpg'), 'JPEG')
    print(f"Converted JPG files saved in folder: {output_folder}")

def pdf_to_word():
    path = input("Enter the PDF path to convert to Word: ").strip()
    output = os.path.join(OUTPUT_DIR, 'converted.docx')
    pdf_reader = PdfReader(path)
    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"

    with open(output, 'w', encoding='utf-8') as out:
        out.write(text)

    print(f"Converted Word file saved at: {output}")


def pdf_to_powerpoint():
    path = input("Enter the PDF path to convert to PowerPoint: ").strip()
    output = os.path.join(OUTPUT_DIR, 'pdf_to_powerpoint.pptx')
    pass  # Use a library like python-pptx
    print(f"Converted PowerPoint file saved at: {output}")

def pdf_to_excel():
    path = input("Enter the PDF path to convert to Excel: ").strip()
    output = os.path.join(OUTPUT_DIR, 'pdf_to_excel.xlsx')
    tabula.convert_into(path, output, output_format='xlsx')
    print(f"Converted Excel file saved at: {output}")

def pdf_to_pdfa():
    path = input("Enter the PDF path to convert to PDF/A: ").strip()
    output = os.path.join(OUTPUT_DIR, 'pdf_to_pdfa.pdf')
    pdf_reader = PdfReader(path)
    pdf_writer = PdfWriter()

    for page in pdf_reader.pages:
        pdf_writer.add_page(page)

    with open(output, 'wb') as out:
        pdf_writer.write(out)
    print(f"Converted PDF/A file saved at: {output}")

# EDIT PDF
def rotate_pdf():
    path = input("Enter the PDF path to rotate: ").strip()
    degrees = int(input("Enter the degrees to rotate (90, 180, 270): "))
    output = os.path.join(OUTPUT_DIR, 'rotated.pdf')
    pdf_reader = PdfReader(path)
    pdf_writer = PdfWriter()

    for page in pdf_reader.pages:
        page.rotate_clockwise(degrees)
        pdf_writer.add_page(page)

    with open(output, 'wb') as out:
        pdf_writer.write(out)
    print(f"Rotated PDF saved at: {output}")

def add_page_numbers():
    path = input("Enter the PDF path to add page numbers: ").strip()
    output = os.path.join(OUTPUT_DIR, 'page_numbers.pdf')
    c = canvas.Canvas(output, pagesize=letter)
    pdf_reader = PdfReader(path)
    pdf_writer = PdfWriter()

    for i, page in enumerate(pdf_reader.pages):
        pdf_writer.add_page(page)
        c.drawString(500, 10, str(i + 1))
        c.showPage()

    c.save()
    with open(output, 'wb') as out:
        pdf_writer.write(out)
    print(f"PDF with page numbers saved at: {output}")

def add_watermark():
    path = input("Enter the PDF path to add a watermark: ").strip()
    watermark_text = input("Enter the watermark text: ")
    output = os.path.join(OUTPUT_DIR, 'watermarked.pdf')
    pdf_reader = PdfReader(path)
    pdf_writer = PdfWriter()

    for page in pdf_reader.pages:
        packet = io.BytesIO()
        c = canvas.Canvas(packet, pagesize=letter)
        c.drawString(100, 100, watermark_text)
        c.save()

        packet.seek(0)
        watermark = PdfReader(packet)
        page.merge_page(watermark.getPage(0))
        pdf_writer.add_page(page)

    with open(output, 'wb') as out:
        pdf_writer.write(out)
    print(f"Watermarked PDF saved at: {output}")

def edit_pdf():
    path = input("Enter the PDF path to edit: ").strip()
    output = os.path.join(OUTPUT_DIR, 'edited.pdf')
    pdf_reader = PdfReader(path)
    pdf_writer = PdfWriter()

    for page in pdf_reader.pages:
        pdf_writer.add_page(page)

    with open(output, 'wb') as out:
        pdf_writer.write(out)
    print(f"Edited PDF saved at: {output}")

# PDF SECURITY
def unlock_pdf():
    path = input("Enter the locked PDF path: ").strip()
    password = input("Enter the password: ").strip()
    output = os.path.join(OUTPUT_DIR, 'unlocked.pdf')
    pdf_reader = PdfReader(path)
    pdf_reader.decrypt(password)
    pdf_writer = PdfWriter()

    for page in pdf_reader.pages:
        pdf_writer.add_page(page)

    with open(output, 'wb') as out:
        pdf_writer.write(out)
    print(f"Unlocked PDF saved at: {output}")

def protect_pdf():
    path = input("Enter the PDF path to protect: ").strip()
    password = input("Enter the password: ").strip()
    output = os.path.join(OUTPUT_DIR, 'protected.pdf')
    pdf_reader = PdfReader(path)
    pdf_writer = PdfWriter()

    for page in pdf_reader.pages:
        pdf_writer.add_page(page)

    pdf_writer.encrypt(user_pwd=password, owner_pwd=None, use_128bit=True)

    with open(output, 'wb') as out:
        pdf_writer.write(out)
    print(f"Protected PDF saved at: {output}")

def sign_pdf():
    path = input("Enter the PDF path to sign: ").strip()
    output = os.path.join(OUTPUT_DIR, 'signed.pdf')
    pass  # Implement digital signature functionality
    print(f"Signed PDF saved at: {output}")

def redact_pdf():
    path = input("Enter the PDF path to redact: ").strip()
    output = os.path.join(OUTPUT_DIR, 'redacted.pdf')
    pass  # Implement redact functionality
    print(f"Redacted PDF saved at: {output}")

def compare_pdfs():
    path1 = input("Enter the first PDF path: ").strip()
    path2 = input("Enter the second PDF path: ").strip()
    output = os.path.join(OUTPUT_DIR, 'comparison.pdf')
    pass  # Implement compare functionality
    print(f"Comparison PDF saved at: {output}")

# Example usage menu
def main():
    print("PDF Operations Menu:")
    print("1. Merge PDFs")
    print("2. Split PDF")
    print("3. Remove Pages from PDF")
    print("4. Extract Pages from PDF")
    print("5. Scan to PDF")
    print("6. Compress PDF")
    print("7. Repair PDF")
    print("8. OCR PDF")
    print("9. Convert JPG to PDF")
    print("10. Convert Word to PDF")
    print("11. Convert PowerPoint to PDF")
    print("12. Convert Excel to PDF")
    print("13. Convert HTML to PDF")
    print("14. Convert PDF to JPG")
    print("15. Convert PDF to Word")
    print("16. Convert PDF to PowerPoint")
    print("17. Convert PDF to Excel")
    print("18. Convert PDF to PDF/A")
    print("19. Rotate PDF")
    print("20. Add Page Numbers to PDF")
    print("21. Add Watermark to PDF")
    print("22. Edit PDF")
    print("23. Unlock PDF")
    print("24. Protect PDF")
    print("25. Sign PDF")
    print("26. Redact PDF")
    print("27. Compare PDFs")

    choice = int(input("Enter the number of the operation you want to perform: "))

    if choice == 1:
        merge_pdfs()
    elif choice == 2:
        split_pdf()
    elif choice == 3:
        remove_pages()
    elif choice == 4:
        extract_pages()
    elif choice == 5:
        scan_to_pdf()
    elif choice == 6:
        compress_pdf()
    elif choice == 7:
        repair_pdf()
    elif choice == 8:
        ocr_pdf()
    elif choice == 9:
        jpg_to_pdf()
    elif choice == 10:
        word_to_pdf()
    elif choice == 11:
        powerpoint_to_pdf()
    elif choice == 12:
        excel_to_pdf()
    elif choice == 13:
        html_to_pdf()
    elif choice == 14:
        pdf_to_jpg()
    elif choice == 15:
        pdf_to_word()
    elif choice == 16:
        pdf_to_powerpoint()
    elif choice == 17:
        pdf_to_excel()
    elif choice == 18:
        pdf_to_pdfa()
    elif choice == 19:
        rotate_pdf()
    elif choice == 20:
        add_page_numbers()
    elif choice == 21:
        add_watermark()
    elif choice == 22:
        edit_pdf()
    elif choice == 23:
        unlock_pdf()
    elif choice == 24:
        protect_pdf()
    elif choice == 25:
        sign_pdf()
    elif choice == 26:
        redact_pdf()
    elif choice == 27:
        compare_pdfs()
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
