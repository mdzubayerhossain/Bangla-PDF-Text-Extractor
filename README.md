**# Bangla-PDF-Text-Extractor**# Bangla PDF Text Extractor

A Python tool for extracting and cleaning Bengali/Bangla text from PDF documents using OCR technology.

## 🌟 Features

- Extracts text from Bangla PDF documents using multiple approaches
- Performs OCR (Optical Character Recognition) optimized for Bengali language
- Intelligently cleans and formats extracted Bangla text
- Fixes common OCR issues with Bengali characters
- Works with both scanned documents and digital PDFs
- Preserves proper word spacing and formatting

## 🔧 Requirements

- Python 3.7+
- Tesseract OCR with Bengali language support
- PyMuPDF (fitz)
- PyTesseract
- Pillow (PIL)
- OpenCV (optional, for image preprocessing)

## 📋 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/bangla-pdf-text-extractor.git
   cd bangla-pdf-text-extractor
   ```

2. Install required Python packages:
   ```bash
   pip install PyMuPDF pytesseract Pillow opencv-python
   ```

3. Install Tesseract OCR with Bengali language support:
   - **Windows:**
     - Download and install Tesseract from [here](https://github.com/UB-Mannheim/tesseract/wiki)
     - During installation, select "Bengali" language pack
     - Add Tesseract to your PATH or update the path in the code
   
   - **macOS:**
     ```bash
     brew install tesseract tesseract-lang
     ```
   
   - **Linux (Ubuntu/Debian):**
     ```bash
     sudo apt-get install tesseract-ocr tesseract-ocr-ben
     ```

4. (Optional) For better word segmentation, install BNLP:
   ```bash
   pip install bnlp-toolkit
   ```

## 🚀 Usage

### Basic Usage

```python
from bangla_pdf_extractor import extract_bangla_text

# Extract text from a PDF file
text = extract_bangla_text("your_file.pdf")

# Save the extracted text to a file
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(text)
```

### CLI Usage

```bash
python extract_bangla.py --input your_file.pdf --output extracted_text.txt
```

## 🛠️ How It Works

1. **PDF Processing**: Opens the PDF using PyMuPDF
2. **Text Extraction**: Attempts direct text extraction first
3. **OCR Processing**: If direct extraction fails, converts pages to images and performs OCR
4. **Text Cleaning**: Applies intelligent cleaning to fix common Bengali OCR issues:
   - Removes unwanted spaces between characters
   - Preserves legitimate spaces between words
   - Fixes punctuation and formatting
5. **Output**: Returns cleaned, readable Bengali text

## 🔄 Common Issues and Solutions

### Characters with spaces between them

If you see output like: "স্ব া স্থ ্য ও প ি র ব া র"

The `smart_clean_bangla_text()` function addresses this by removing spaces between characters while preserving word boundaries.

### Words running together

If you see output like: "এবংস্বাস্থ্যওপরিবারকল্যাণমন্ত্রণালয়গুরুত্বপূর্ণভূমিকাপালনকরে"

The word segmentation feature uses linguistic rules or the BNLP library to properly separate words.

## 📝 Examples

### Extract and save text from a PDF:

```python
from bangla_pdf_extractor import extract_bangla_text_improved

# Extract text with improved cleaning
text = extract_bangla_text_improved("document.pdf")

# Save to file
with open("extracted_text.txt", "w", encoding="utf-8") as f:
    f.write(text)
```

### Process multiple PDFs:

```python
import os
from bangla_pdf_extractor import extract_bangla_text_improved

pdf_dir = "pdf_files"
output_dir = "extracted_text"

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Process each PDF file
for pdf_file in os.listdir(pdf_dir):
    if pdf_file.endswith(".pdf"):
        input_path = os.path.join(pdf_dir, pdf_file)
        output_path = os.path.join(output_dir, f"{os.path.splitext(pdf_file)[0]}.txt")
        
        print(f"Processing: {pdf_file}")
        text = extract_bangla_text_improved(input_path)
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)
        
        print(f"Saved to: {output_path}")
```

## 🤝 Contributing

Contributions are welcome! If you'd like to improve the Bangla PDF Text Extractor:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for the OCR engine
- [PyMuPDF](https://github.com/pymupdf/PyMuPDF) for PDF processing
- [BNLP](https://github.com/sagorbrur/bnlp) for Bengali NLP tools
