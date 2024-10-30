import PyPDF2

def merge_pdfs_alternatively(pdf1_path, pdf2_path, output_path):
    # Open the PDF files
    pdf1 = open(pdf1_path, 'rb')
    pdf2 = open(pdf2_path, 'rb')

    # Read the PDFs
    reader1 = PyPDF2.PdfReader(pdf1)
    reader2 = PyPDF2.PdfReader(pdf2)

    # Create a PDF writer to save the combined PDF
    writer = PyPDF2.PdfWriter()

    # Get the total number of pages in both PDFs
    total_pages = max(len(reader1.pages), len(reader2.pages))

    # Add pages alternatively from both PDFs
    for i in range(total_pages):
        if i < len(reader1.pages):
            writer.add_page(reader1.pages[i])
        if i < len(reader2.pages):
            writer.add_page(reader2.pages[i])

    # Write the output to a new PDF file
    with open(output_path, 'wb') as output_pdf:
        writer.write(output_pdf)

    # Close the input PDFs
    pdf1.close()
    pdf2.close()

    print(f'Merged PDF saved as: {output_path}')

# Example usage:
merge_pdfs_alternatively('pdf1.pdf', 'pdf2.pdf', 'new.pdf')
