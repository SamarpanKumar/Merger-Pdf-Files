from PyPDF2 import PdfWriter
import os

# Create a PdfWriter object
merger = PdfWriter()

# List of PDF files in the "merged-pdf" directory
files = [file for file in os.listdir("merged-pdf") if file.endswith(".pdf")]

# Sort files if needed, to ensure they are merged in a specific order
files.sort()

# Append each PDF file to the merger
for pdf in files:
    # Provide the full path to the PDF file
    merger.append(os.path.join("merged-pdf", pdf))

# Write the merged PDF to a file
output_path = "merged-pdf.pdf"
with open(output_path, "wb") as output_file:
    merger.write(output_file)

# Close the merger
merger.close()

print(f"Merged {len(files)} PDF files into {output_path}")
