"""
Analyze Meezan deposit slip number patterns
"""
import pdfplumber

MEEZAN_PATH = r"E:\FC\FC Enterprises\FC RECON\DS Dec-25 & Jan-26\FCPL-MEEZAN Dec'25 & Jan'26 BS.pdf"

print("=" * 80)
print("MEEZAN DEPOSIT SLIP NUMBER ANALYSIS")
print("=" * 80)

with pdfplumber.open(MEEZAN_PATH) as pdf:
    text = pdf.pages[0].extract_text() + "\n" + pdf.pages[1].extract_text()
    
    lines = text.split('\n')
    
    print("\nDeposit Transactions:")
    print("-" * 80)
    
    in_deposit = False
    deposit_lines = []
    
    for i, line in enumerate(lines):
        line_stripped = line.strip()
        
        # Look for deposit transactions
        if 'Online Cash Deposit' in line_stripped or 'Online Deposit' in line_stripped:
            in_deposit = True
            deposit_lines = [(i, line_stripped)]
        elif in_deposit and line_stripped:
            # Skip if it's a new transaction with date
            import re
            if not re.match(r'^\d{2}/\d{2}', line_stripped):
                deposit_lines.append((i, line_stripped))
            else:
                # New transaction - print previous
                print(f"\nTransaction:")
                for line_num, content in deposit_lines:
                    print(f"  Line {line_num}: {content}")
                
                # Extract potential slip numbers
                print(f"  Potential Slip Numbers:")
                for line_num, content in deposit_lines[1:]:  # Skip first line (has amount)
                    # Find all numbers and alphanumeric codes
                    import re
                    # Find numbers in parentheses
                    paren_nums = re.findall(r'\((\d+)\)', content)
                    # Find standalone numbers (4+ digits)
                    standalone_nums = re.findall(r'\b(\d{4,})\b', content)
                    # Find alphanumeric like 13D
                    alphanumeric = re.findall(r'\b(\d+[A-Z])\b', content, re.IGNORECASE)
                    
                    if paren_nums:
                        print(f"    Branch Code: {paren_nums}")
                    if alphanumeric:
                        print(f"    Alphanumeric: {alphanumeric}")
                    if standalone_nums:
                        print(f"    Numbers: {standalone_nums}")
                
                in_deposit = False
                deposit_lines = []
        
        # Limit output
        if len([x for x in deposit_lines if 'Deposit' in x[1]]) > 5:
            break
