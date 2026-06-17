import os

dir_path = r'F:\Raptureholidaysllpsite\travela-1.0.0\fr'
search = bytes([0xC3, 0x83, 0xC2, 0xA9])
replace = bytes([0xC3, 0xA9])
count = 0
for fname in sorted(os.listdir(dir_path)):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(dir_path, fname)
    with open(fpath, 'rb') as f:
        content = f.read()
    if search in content:
        new = content.replace(search, replace)
        with open(fpath, 'wb') as f:
            f.write(new)
        print(f'Fixed: {fname} ({content.count(search)} occurrences)')
        count += 1
    else:
        print(f'Clean: {fname}')
print(f'Done, updated {count} files')
