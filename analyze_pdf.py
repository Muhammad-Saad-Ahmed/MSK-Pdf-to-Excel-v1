"""
Analyze PDF structure to understand the actual format
"""
import pdfplumber
import os

PDF_PATH = r"E:\FC\FC Enterprises\FC RECON\DS Dec-25 & Jan-26\FC ENT HBL Dec'25 & Jan'26 BS.pdf"

print("=" * 80)
print("PDF STRUCTURE ANALYSIS")
print("=" * 80)

with pdfplumber.open(PDF_PATH) as pdf:
    print(f"\nTotal Pages: {len(pdf.pages)}\n")
    
    # Analyze first 3 pages
    for i, page in enumerate(pdf.pages[:3]):
        print(f"\n{'='*80}")
        print(f"PAGE {i+1}")
        print(f"{'='*80}")
        
        # Extract text
        text = page.extract_text()
        print("\n--- RAW TEXT ---")
        print(text[:3000] if text else "NO TEXT")
        
        # Extract tables
        print("\n--- TABLES ---")
        tables = page.extract_tables()
        for j, table in enumerate(tables):
            print(f"\nTable {j+1}:")
            for row in table[:15]:  # First 15 rows
                print(row)
        
        # Extract words with positions
        print("\n--- WORDS (first 50) ---")
        words = page.extract_words()
        for word in words[:50]:
            print(f"x={word['x0']:.0f}, y={word['top']:.0f}: {word['text']}")

print("\n" + "=" * 80)
print("ANALYSIS COMPLETE")
print("=" * 80)
