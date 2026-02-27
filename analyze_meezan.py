"""
Analyze Meezan Bank PDF structure
"""
import pdfplumber

PDF_PATH = r"E:\FC\FC Enterprises\FC RECON\DS Dec-25 & Jan-26\FCPL-MEEZAN Dec'25 & Jan'26 BS.pdf"

print("=" * 80)
print("MEEZAN BANK STRUCTURE ANALYSIS")
print("=" * 80)

with pdfplumber.open(PDF_PATH) as pdf:
    print(f"\nTotal Pages: {len(pdf.pages)}\n")
    
    # Analyze first 3 pages
    for i, page in enumerate(pdf.pages[:2]):
        print(f"\n{'='*80}")
        print(f"PAGE {i+1}")
        print(f"{'='*80}")
        
        text = page.extract_text()
        print("\n--- RAW TEXT (first 3000 chars) ---")
        print(text[:3000])
        
        # Show lines with transactions
        print("\n--- TRANSACTION LINES ---")
        lines = text.split('\n')
        for j, line in enumerate(lines[:50]):
            if any(keyword in line.upper() for keyword in ['DEC', 'JAN', 'DEPOSIT', 'TRANSFER', 'CHEQUE']):
                print(f"Line {j}: {line}")
