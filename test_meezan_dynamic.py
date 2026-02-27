"""
Test Meezan dynamic particulars columns
"""
import sys
sys.path.insert(0, r'E:\hackthaon\PDF to Excel Converter')

from app import parse_meezan, extract_text_with_pdfplumber, generate_excel

MEEZAN_PATH = r"E:\FC\FC Enterprises\FC RECON\DS Dec-25 & Jan-26\FCPL-MEEZAN Dec'25 & Jan'26 BS.pdf"

print("=" * 80)
print("TESTING MEEZAN DYNAMIC PARTICULARS")
print("=" * 80)

text = extract_text_with_pdfplumber(MEEZAN_PATH)
transactions = parse_meezan(text)

print(f"\nTotal Transactions: {len(transactions)}\n")

# Find max particulars in any transaction
max_parts = 0
max_txn_idx = 0

for i, txn in enumerate(transactions):
    particulars_list = txn.get('particulars_list', [])
    total_parts = 0
    for p in particulars_list:
        parts = [part.strip() for part in p.split() if part.strip()]
        total_parts += len(parts)
    if total_parts > max_parts:
        max_parts = total_parts
        max_txn_idx = i

print(f"Maximum Particulars in a single transaction: {max_parts}")
print(f"\nTransaction with max particulars (#{max_txn_idx + 1}):")

txn = transactions[max_txn_idx]
print(f"  Date: {txn['date']}")
print(f"  Credit: {txn['credit']}, Debit: {txn['debit']}")
print(f"  Particulars Lines ({len(txn['particulars_list'])}):")
for i, p in enumerate(txn['particulars_list']):
    print(f"    [{i}] {p}")

# Show flattened parts
all_parts = []
for p in txn['particulars_list']:
    parts = [part.strip() for part in p.split() if part.strip()]
    all_parts.extend(parts)

print(f"\n  Flattened Parts ({len(all_parts)}):")
for i, part in enumerate(all_parts[:15]):
    print(f"    Particulars{i+1}: {part}")

# Generate Excel
print("\n" + "=" * 80)
print("GENERATING EXCEL WITH DYNAMIC COLUMNS")
print("=" * 80)

excel_bytes = generate_excel(transactions, "Meezan Bank")

output_path = r"C:\Users\Admin\Downloads\meezan_dynamic.xlsx"
with open(output_path, 'wb') as f:
    f.write(excel_bytes)

print(f"\nExcel saved to: {output_path}")
print(f"Columns: Date, Credit, Debit, Bank, Particulars1 to Particulars{max_parts}")
