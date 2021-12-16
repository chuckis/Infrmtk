import os

filepaths = []

for subdir, dirs, files in os.walk("5-k"):
    for filename in files:
        filepath = subdir + os.sep + filename
        if filepath.endswith(".md"):
            filepaths.append(filepath)

lines = []
filepaths.sort()
for file in filepaths:
    with open(file, 'r', encoding='utf8', errors='ignore') as lesson:
        for line in lesson:
            if line.startswith("# "):
                lines.append(line)

filepaths.sort()
print(filepaths)
for line in lines:
    print(line)