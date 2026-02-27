"""
Analyze HBL line structure for proper amount extraction
"""
import re
import pdfplumber

PDF_PATH = r"E:\FC\FC Enterprises\FC RECON\DS Dec-25 & Jan-26\FC ENT HBL Dec'25 & Jan'26 BS.pdf"

print("=" * 80)
print("HBL LINE STRUCTURE ANALYSIS")
print("=" * 80)

with pdfplumber.open(PDF_PATH) as pdf:
    page = pdf.pages[1]
    text = page.extract_text()
    
    lines = text.split('\n')
    
    print("\nSample transaction lines:")
    print("-" * 80)
    
    for i, line in enumerate(lines):
        if 'Online Deposit' in line or 'CHQ Dr' in line or 'Funds Transfer' in line:
            print(f"\nLine {i+1}:")
            print(f"  Raw: {repr(line)}")
            print(f"  Display: {line}")
            
            # Split by pipe to see columns
            cols = line.split('|')
            print(f"  Columns ({len(cols)}):")
            for j, col in enumerate(cols):
                print(f"    [{j}]: '{col.strip()}'")
