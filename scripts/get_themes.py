import os
import re

filepaths = []

for subdir, dirs, files in os.walk("6-k"):
    for filename in files:
        filepath = subdir + os.sep + filename
        if filename.startswith("urok"):
            filepaths.append(filepath)

lines = []

def sort_nicely( l ):
    """ Sort the given list in the way that humans expect.
    """
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    l.sort( key=alphanum_key )

sort_nicely(filepaths)

for file in filepaths:
    with open(file, 'r', encoding='utf8', errors='ignore') as lesson:
        for line in lesson:
            if line.startswith("# "):
                lines.append(line)


print(filepaths)
for line in lines:
    print(line)