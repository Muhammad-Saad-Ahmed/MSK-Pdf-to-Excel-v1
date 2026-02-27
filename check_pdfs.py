"""
Check if PDFs are text-based or image-based
"""
import os
import pdfplumber

PDF_FOLDER = r"E:\FC\FC Enterprises\FC RECON\DS Dec-25 & Jan-26"

def check_pdf_type(pdf_path):
    """Check if PDF is text-based or image-based"""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            total_text = ""
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    total_text += text
            
            if total_text.strip():
                # Check if we got meaningful text
                words = total_text.split()
                if len(words) > 10:
                    return "TEXT-BASED", len(words)
                else:
                    return "IMAGE-BASED (OCR needed)", 0
            else:
                return "IMAGE-BASED (OCR needed)", 0
    except Exception as e:
        return f"ERROR: {str(e)}", 0

print("=" * 70)
print("PDF TYPE CHECKER")
print("=" * 70)
print(f"Folder: {PDF_FOLDER}\n")

pdf_files = [f for f in os.listdir(PDF_FOLDER) if f.lower().endswith('.pdf')]

if not pdf_files:
    print("No PDF files found!")
else:
    print(f"Found {len(pdf_files)} PDF files:\n")
    
    results = []
    for pdf in pdf_files:
        pdf_path = os.path.join(PDF_FOLDER, pdf)
        pdf_type, word_count = check_pdf_type(pdf_path)
        results.append((pdf, pdf_type, word_count))
        
        status = "[OK]" if "TEXT" in pdf_type else "[IMAGE]"
        print(f"{status} {pdf}")
        print(f"  Type: {pdf_type}")
        print(f"  Words extracted: {word_count}")
        print()
    
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    text_based = [r[0] for r in results if "TEXT" in r[1]]
    image_based = [r[0] for r in results if "IMAGE" in r[1]]
    
    print(f"\nTEXT-BASED PDFs ({len(text_based)}):")
    for f in text_based:
        print(f"  [OK] {f}")
    
    print(f"\nIMAGE-BASED PDFs ({len(image_based)}):")
    for f in image_based:
        print(f"  [IMAGE] {f}")
    
    if not image_based:
        print("\n[OK] All PDFs are text-based! Tesseract/Poppler NOT required.")
    else:
        print("\n[WARNING] Some PDFs are image-based. Tesseract/Poppler REQUIRED for these.")
