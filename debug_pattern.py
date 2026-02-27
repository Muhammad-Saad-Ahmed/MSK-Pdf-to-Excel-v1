"""
Debug the date pattern matching
"""
import re
import pdfplumber

PDF_PATH = r"E:\FC\FC Enterprises\FC RECON\DS Dec-25 & Jan-26\FC ENT HBL Dec'25 & Jan'26 BS.pdf"

print("=" * 80)
print("DEBUGGING DATE PATTERN")
print("=" * 80)

with pdfplumber.open(PDF_PATH) as pdf:
    # Get first transaction page (page 2)
    page = pdf.pages[1]
    text = page.extract_text()
    
    print("\nFirst 2000 chars of text:")
    print("-" * 80)
    print(text[:2000])
    print("-" * 80)
    
    # Test date pattern
    date_pattern = r'(\d{1,2}(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)\d{2})'
    
    print("\n\nSearching for dates with pattern:")
    print(f"  {date_pattern}")
    print("\nMatches found:")
    
    matches = re.findall(date_pattern, text, re.IGNORECASE)
    for match in matches[:20]:
        print(f"  - {match}")
    
    # Search line by line
    print("\n\nLine by line analysis:")
    lines = text.split('\n')
    for i, line in enumerate(lines[:30]):
        line = line.strip()
        if not line:
            continue
        
        date_match = re.match(date_pattern, line, re.IGNORECASE)
        if date_match:
            print(f"\nLine {i+1}: FOUND DATE '{date_match.group(1)}'")
            print(f"  Content: {line[:100]}")
        elif 'DEC' in line.upper() or 'JAN' in line.upper():
            print(f"\nLine {i+1}: Contains month but no match")
            print(f"  Content: {line[:100]}")
