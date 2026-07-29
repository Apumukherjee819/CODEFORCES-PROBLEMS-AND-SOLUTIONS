import sys
import re

def column_to_number(col):
    value = 0
    for ch in col:
        value = value * 26 + (ord(ch) - ord('A') + 1)
    return value

def number_to_column(num):
    result = []
    while num > 0:
        num -= 1
        result.append(chr(num % 26 + ord('A')))
        num //= 26
    return ''.join(reversed(result))

n = int(sys.stdin.readline())

for _ in range(n):
    s = sys.stdin.readline().strip()

    # Format: R<row>C<column>, e.g. R23C55
    match = re.fullmatch(r'R(\d+)C(\d+)', s)

    if match:
        row = match.group(1)
        col_num = int(match.group(2))
        print(number_to_column(col_num) + row)
    else:
        # Format: <letters><row>, e.g. BC23
        match = re.fullmatch(r'([A-Z]+)(\d+)', s)
        col_letters = match.group(1)
        row = match.group(2)

        print(f"R{row}C{column_to_number(col_letters)}")
