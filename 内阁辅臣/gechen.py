## 爬取明朝内阁辅臣的scrapy爬虫

import re
import json
import requests
from bs4 import BeautifulSoup

def rename_arg(arg):
    s = arg.replace('\n',' ')
    s1, _ = re.subn(r"\[.*\]", "", s)
    return s1

r = requests.get("https://zh.wikipedia.org/wiki/%E6%98%8E%E6%9C%9D%E5%86%85%E9%98%81%E8%BE%85%E8%87%A3%E5%B9%B4%E8%A1%A8")

soup = BeautifulSoup(r.text, "lxml")

tables = soup.find_all("table", {"class": "wikitable"})
print("size of tables : ", len(tables))

dict = {}
global_cnt = 1
for i in range(len(tables)):
    items = tables[i].find_all('td')
    print("size of items : ", len(items))
    if len(items) == 193:
        del items[104]

    step = 4

    for base_index in range(0, len(items), step):
        year_key = items[base_index].text.replace('\n', '')

        shoufu = "内阁首辅"
        fuchen = "内阁辅臣"
        beijing = "背景"

        dict[year_key] = {  "序号":global_cnt,
                            shoufu:rename_arg(items[base_index + 1].text),
                            fuchen:rename_arg(items[base_index + 2].text),
                            beijing:rename_arg(items[base_index + 3].text),
                        }
        global_cnt += 1


# dict_json = json.dumps(dict, ensure_ascii=False)
with open('fuchen.json', 'w') as outfile:
    json.dump(dict, outfile, ensure_ascii=False)
