
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import os
import re
import bnlp  # Bengali NLP library

def smart_clean_bangla_text(text):
    """Clean Bangla text with intelligent spacing"""
    # First clean up and normalize the text
    text = re.sub(r'\s+', ' ', text).strip()
    
    try:
        # Try using bnlp for tokenization if available
        from bnlp import NLTKTokenizer
        tokenizer = NLTKTokenizer()
        words = tokenizer.word_tokenize(text)
        return ' '.join(words)
    except (ImportError, Exception):
        # Fall back to simple rule-based approach
        # Remove spaces between Bangla characters
        bangla_char_pattern = r'([\u0980-\u09FF])\s+([\u0980-\u09FF])'
        while re.search(bangla_char_pattern, text):
            text = re.sub(bangla_char_pattern, r'\1\2', text)
        
        # Add spaces after punctuation
        text = re.sub(r'([।,;:!?])', r'\1 ', text)
        
        # Common conjunctions
        for conj in ['এবং', 'ও', 'কিন্তু']:
            text = re.sub(f'([^\s]){conj}', f'\\1 {conj}', text)
            text = re.sub(f'{conj}([^\s])', f'{conj} \\1', text)
            
        # Clean up spaces
        text = re.sub(r'\s+', ' ', text).strip()
        return text

def extract_bangla_text_improved(pdf_path):
    """Extract and clean Bangla text from PDF"""
    # Configure tesseract
    if os.name == 'nt':  # Windows
        tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        if os.path.exists(tesseract_path):
            pytesseract.pytesseract.tesseract_cmd = tesseract_path
    
    # Open PDF with PyMuPDF
    doc = fitz.open(pdf_path)
    extracted_text = ""
    
    for page_num in range(len(doc)):
        print(f"Processing page {page_num + 1}/{len(doc)}")
        page = doc[page_num]
        
        # Try direct text extraction first
        page_text = page.get_text()
        
        # If direct extraction returned decent text, use it
        if len(page_text.strip()) > 50:
            extracted_text += page_text + "\n\n"
            continue
        
        # Otherwise use OCR
        pix = page.get_pixmap(dpi=300)
        temp_img_path = f"temp_page_{page_num}.png"
        pix.save(temp_img_path)
        
        # OCR with Bengali settings
        custom_config = r'--oem 3 --psm 6 -l ben+eng'
        img = Image.open(temp_img_path)
        ocr_text = pytesseract.image_to_string(img, config=custom_config)
        extracted_text += ocr_text + "\n\n"
        
        # Clean up temp file
        os.remove(temp_img_path)
    
    # Clean the text
    cleaned_text = smart_clean_bangla_text(extracted_text)
    
    return cleaned_text

# Usage
if __name__ == "__main__":
    pdf_file = "bangla.pdf"  # Update with your file path
    cleaned_text = extract_bangla_text_improved(pdf_file)
    
    with open("bangla_text_cleaned.txt", "w", encoding="utf-8") as f:
        f.write(cleaned_text)
    
    print("Text extraction and cleaning complete")
