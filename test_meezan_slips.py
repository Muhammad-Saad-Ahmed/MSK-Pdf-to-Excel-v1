"""
Test Meezan slip number extraction
"""
import sys
sys.path.insert(0, r'E:\hackthaon\PDF to Excel Converter')

from app import parse_meezan, extract_text_with_pdfplumber, generate_excel

MEEZAN_PATH = r"E:\FC\FC Enterprises\FC RECON\DS Dec-25 & Jan-26\FCPL-MEEZAN Dec'25 & Jan'26 BS.pdf"

print("=" * 80)
print("TESTING MEEZAN SLIP NUMBER EXTRACTION")
print("=" * 80)

text = extract_text_with_pdfplumber(MEEZAN_PATH)
transactions = parse_meezan(text)

print(f"\nTotal Transactions: {len(transactions)}\n")

# Show deposit transactions with slip numbers
print("DEPOSIT TRANSACTIONS WITH SLIP NUMBERS:")
print("-" * 80)

deposit_count = 0
for i, txn in enumerate(transactions):
    if txn['slip_numbers'] or 'Deposit' in str(txn.get('particulars_list', [])):
        deposit_count += 1
        if deposit_count <= 10:  # Show first 10
            print(f"\n{i+1}. Date: {txn['date']}")
            print(f"   Credit: {txn['credit']}, Debit: {txn['debit']}")
            print(f"   Slip Numbers ({len(txn['slip_numbers'])}): {txn['slip_numbers']}")
            print(f"   Particulars: {txn['particulars_list'][:3]}")

# Generate Excel
print("\n" + "=" * 80)
print("GENERATING EXCEL")
print("=" * 80)

excel_bytes = generate_excel(transactions, "Meezan Bank")

output_path = r"C:\Users\Admin\Downloads\meezan_with_slips.xlsx"
with open(output_path, 'wb') as f:
    f.write(excel_bytes)

print(f"\nExcel saved to: {output_path}")
print(f"Total transactions: {len(transactions)}")
print(f"Transactions with slip numbers: {sum(1 for t in transactions if t['slip_numbers'])}")
