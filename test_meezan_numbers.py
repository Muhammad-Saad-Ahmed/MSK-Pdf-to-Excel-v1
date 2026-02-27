"""
Test Meezan number extraction
"""
import sys
sys.path.insert(0, r'E:\hackthaon\PDF to Excel Converter')

from app import parse_meezan, extract_text_with_pdfplumber, generate_excel

MEEZAN_PATH = r"E:\FC\FC Enterprises\FC RECON\DS Dec-25 & Jan-26\FCPL-MEEZAN Dec'25 & Jan'26 BS.pdf"

print("=" * 80)
print("TESTING MEEZAN NUMBER EXTRACTION")
print("=" * 80)

text = extract_text_with_pdfplumber(MEEZAN_PATH)
transactions = parse_meezan(text)

print(f"\nTotal Transactions: {len(transactions)}\n")

# Show first 15 transactions
print("FIRST 15 TRANSACTIONS:")
print("-" * 80)

for i, txn in enumerate(transactions[:15]):
    print(f"\n{i+1}. Date: {txn['date']}")
    print(f"   Credit: {txn['credit']}, Debit: {txn['debit']}")
    print(f"   Particulars Numbers ({len(txn['particulars_numbers'])}): {txn['particulars_numbers']}")

# Generate Excel
print("\n" + "=" * 80)
print("GENERATING EXCEL")
print("=" * 80)

excel_bytes = generate_excel(transactions, "Meezan Bank")

output_path = r"C:\Users\Admin\Downloads\meezan_numbers_only.xlsx"
with open(output_path, 'wb') as f:
    f.write(excel_bytes)

print(f"\nExcel saved to: {output_path}")
print(f"Total transactions: {len(transactions)}")
