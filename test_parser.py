"""
Test the HBL parser with actual PDF
"""
import sys
sys.path.insert(0, r'E:\hackthaon\PDF to Excel Converter')

from app import parse_hbl, extract_text_with_pdfplumber, generate_excel
import os

PDF_PATH = r"E:\FC\FC Enterprises\FC RECON\DS Dec-25 & Jan-26\FC ENT HBL Dec'25 & Jan'26 BS.pdf"

print("=" * 80)
print("TESTING HBL PARSER")
print("=" * 80)

# Extract text
print("\nExtracting text from PDF...")
text = extract_text_with_pdfplumber(PDF_PATH)
print(f"Extracted {len(text)} characters")

# Parse
print("\nParsing transactions...")
transactions = parse_hbl(text)
print(f"Found {len(transactions)} transactions\n")

# Show first 10 transactions with particulars
print("=" * 80)
print("FIRST 10 TRANSACTIONS:")
print("=" * 80)
for i, txn in enumerate(transactions[:10]):
    print(f"\n{i+1}. Date: {txn['date']}")
    print(f"   Particulars ({len(txn['particulars_list'])} lines):")
    for j, p in enumerate(txn['particulars_list'][:5]):
        print(f"      [{j}] {p}")
    print(f"   Credit: {txn['credit']}")
    print(f"   Debit: {txn['debit']}")

# Generate Excel
print("\n" + "=" * 80)
print("GENERATING EXCEL...")
print("=" * 80)
excel_bytes = generate_excel(transactions, "Habib Bank Limited")

# Save for inspection
output_path = r"C:\Users\Admin\Downloads\bank_statement_test.xlsx"
with open(output_path, 'wb') as f:
    f.write(excel_bytes)

print(f"\nExcel saved to: {output_path}")
print(f"Total transactions: {len(transactions)}")
