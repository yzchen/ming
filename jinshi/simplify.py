import os
import fileinput
from langconv import *

for filename in os.listdir('./'):
    os.rename(filename, Traditional2Simplified(filename))

for filename in os.listdir('./'):
    if '.json' in filename:
        with open(filename, 'r', encoding='utf-8') as f, open('data/'+filename, 'w', encoding='utf-8') as fd:
            lines = f.readlines()
            for i in range(len(lines)):
                lines[i] = Traditional2Simplified(lines[i])
                fd.write(lines[i])
