"""
Test HBL and Meezan parsers
"""
import sys
sys.path.insert(0, r'E:\hackthaon\PDF to Excel Converter')

from app import parse_hbl, parse_meezan, extract_text_with_pdfplumber, generate_excel, detect_bank

HBL_PATH = r"E:\FC\FC Enterprises\FC RECON\DS Dec-25 & Jan-26\FC ENT HBL Dec'25 & Jan'26 BS.pdf"
MEEZAN_PATH = r"E:\FC\FC Enterprises\FC RECON\DS Dec-25 & Jan-26\FCPL-MEEZAN Dec'25 & Jan'26 BS.pdf"

print("=" * 80)
print("TESTING HBL PARSER")
print("=" * 80)

text = extract_text_with_pdfplumber(HBL_PATH)
bank = detect_bank(text)
print(f"Detected Bank: {bank}")

transactions = parse_hbl(text)
print(f"Transactions: {len(transactions)}\n")

for i, txn in enumerate(transactions[:3]):
    print(f"{i+1}. Date: {txn['date']}")
    print(f"   Particulars: {txn['particulars_list'][:3]}")
    print(f"   Credit: {txn['credit']}, Debit: {txn['debit']}")

print("\n" + "=" * 80)
print("TESTING MEEZAN PARSER")
print("=" * 80)

text = extract_text_with_pdfplumber(MEEZAN_PATH)
bank = detect_bank(text)
print(f"Detected Bank: {bank}")

transactions = parse_meezan(text)
print(f"Transactions: {len(transactions)}\n")

for i, txn in enumerate(transactions[:5]):
    print(f"{i+1}. Date: {txn['date']}")
    print(f"   Particulars: {txn['particulars_list'][:3]}")
    print(f"   Credit: {txn['credit']}, Debit: {txn['debit']}")

# Generate Excel for Meezan
print("\n" + "=" * 80)
print("GENERATING MEEZAN EXCEL")
print("=" * 80)

transactions = parse_meezan(extract_text_with_pdfplumber(MEEZAN_PATH))
excel_bytes = generate_excel(transactions, "Meezan Bank")

output_path = r"C:\Users\Admin\Downloads\meezan_test.xlsx"
with open(output_path, 'wb') as f:
    f.write(excel_bytes)

print(f"\nExcel saved to: {output_path}")
print(f"Total transactions: {len(transactions)}")
