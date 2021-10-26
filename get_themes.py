import os

filepaths = []

for subdir, dirs, files in os.walk(r'.'):
    for filename in files:
        filepath = subdir + os.sep + filename
        if filepath.endswith(".md"):
            filepaths.append(filepath)

lines = []

for file in filepaths:
    with open(file, 'r', encoding='utf8', errors='ignore') as lesson:
        for line in lesson:
            if line.startswith("# "):
                lines.append(line)

print(lines, len(lines))