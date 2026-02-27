"""
Analyze PARTICULARS structure in detail
"""
import pdfplumber

PDF_PATH = r"E:\FC\FC Enterprises\FC RECON\DS Dec-25 & Jan-26\FC ENT HBL Dec'25 & Jan'26 BS.pdf"

print("=" * 80)
print("PARTICULARS STRUCTURE ANALYSIS")
print("=" * 80)

with pdfplumber.open(PDF_PATH) as pdf:
    page = pdf.pages[1]
    text = page.extract_text()
    
    lines = text.split('\n')
    
    print("\nTransaction with multi-line particulars:")
    print("-" * 80)
    
    # Find a transaction and show all its lines
    in_transaction = False
    txn_lines = []
    
    for i, line in enumerate(lines):
        if '02DEC25' in line and 'Online Deposit 31064582' in line:
            in_transaction = True
        
        if in_transaction:
            txn_lines.append((i, line))
            # Next transaction starts
            if '03DEC25' in line and 'Online Deposit' in line:
                break
    
    for line_num, line in txn_lines:
        print(f"Line {line_num}: {repr(line)}")
        print(f"        {line}")
        print()
