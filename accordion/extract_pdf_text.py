import pdfplumber

# Path to your PDF file
pdf_path = r"C:\Users\user\Desktop\javascript\accordion\accordion\computer graphics written note.pdf"

# Output text file
output_path = "extracted_text.txt"

try:
    with pdfplumber.open(pdf_path) as pdf:
        all_text = ""
        for page in pdf.pages:
            all_text += page.extract_text() + "\n"
        # Save the extracted text to a file
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(all_text)
        print(f"Text successfully extracted to {output_path}")
except Exception as e:
    print(f"An error occurred: {e}")
