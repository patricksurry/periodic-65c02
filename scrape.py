import pandas as pd
import json


def parse_cell(s, opcode):
    """parse text like 'BCC r8 2 3+/2 ------' """
    if pd.isna(s):
        return None
    parts = s.split()
    m = parts[0]
    arg = parts[1] if len(parts) == 5 else None
    n, cycles, flags = parts[-3:]
    return dict(opcode=opcode, mnemonic=m, arg=arg, bytes=int(n), cycles=cycles, flags=flags)

ts = pd.read_html('https://pastraiser.com/cpu/6502/6502_opcodes.html')

df = ts[0]

print(df)

opcodes = [
    parse_cell(df[l+1][h+1], opcode=f'{(h<<4)+l:02x}')
    for h in range(16)
    for l in range(16)
]

json.dump(opcodes, open('opcodes.json', 'w'), indent=4)
