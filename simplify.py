import os
import fileinput
import argparse
from langconv import *

def Simple2Traditional(line):
    #将简体转换成繁体
    line = Converter('zh-hant').convert(line)
    return line

def Traditional2Simplified(line):
    # 将繁体转换成简体
    line = Converter('zh-hans').convert(line)
    return line

parser = argparse.ArgumentParser(description='convert traditional Chinese json files under given folder to Simplified version')
parser.add_argument('directory', metavar='dir', type=str,
                   help='a directory name based on current path')

args = parser.parse_args()
print(args.directory)

# for file name
for filename in os.listdir(os.path.join('.', args.directory)):
    os.rename(filename, Traditional2Simplified(filename))

# for file content
for filename in os.listdir(os.path.join('.', args.directory)):
    if '.json' in filename:
        with open(filename, 'r', encoding='utf-8') as f, open('./data/'+filename, 'w', encoding='utf-8') as fd:
            lines = f.readlines()
            for i in range(len(lines)):
                lines[i] = Traditional2Simplified(lines[i])
                fd.write(lines[i])
