import os

dir_path = r'F:\Raptureholidaysllpsite\travela-1.0.0\fr'
count = 0
for fname in sorted(os.listdir(dir_path)):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(dir_path, fname)
    with open(fpath, 'rb') as f:
        content = f.read()
    replaced = bytearray(content)
    i = 0
    changes = 0
    while i < len(replaced) - 3:
        if replaced[i] == 0xC3 and replaced[i+1] == 0x83 and replaced[i+2] == 0xC2 and i+3 < len(replaced):
            # Replace C3 83 C2 XX with C3 XX (fix double-encoding)
            replaced[i+1] = 0x83  # keep overhead byte (will be removed below)
            replaced = replaced[:i+1] + replaced[i+3:]
            changes += 1
        else:
            i += 1
    if changes:
        with open(fpath, 'wb') as f:
            f.write(bytes(replaced))
        print(f'Fixed {changes} chars in {fname}')
        count += 1
    else:
        print(f'Clean: {fname}')
print(f'Done. Updated {count} files')
