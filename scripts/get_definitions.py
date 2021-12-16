import os
import re

filepaths = []

for root, dirs, files in os.walk("5-k", topdown = False):
   for name in files:
       filepaths.append(os.path.join(root, name))


lines = []

definitionregex = re.compile(r'\*{2}(.*?)\*{2}')
definitions = ''

# get all definitions from lessons
for file in filepaths:
    with open(file, 'r', encoding='utf8', errors='ignore') as lesson:
        definition = definitionregex.findall(lesson.read())
        if definition:
            definitions+=str(definition).strip()
            
print(definitions)
