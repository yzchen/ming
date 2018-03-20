## 爬取明朝六部尚书+都御史的scrapy爬虫

import re
import json
import requests
from bs4 import BeautifulSoup

def rename_arg(arg):
    s = arg.replace('\n',' ').replace('左都御史', '(左都御史)').replace('右都御史', '(右都御史)').replace('署', '(署)')
    s1, _ = re.subn(r"\[.*\]", "", s)
    return s1

r = requests.get("https://zh.wikipedia.org/wiki/%E6%98%8E%E6%9C%9D%E5%B0%9A%E4%B9%A6%E4%B8%8E%E9%83%BD%E5%BE%A1%E5%8F%B2%E5%B9%B4%E8%A1%A8")

soup = BeautifulSoup(r.text, "lxml")

tables = soup.find_all("table", {"class": "wikitable"})
print("size of tables : ", len(tables))

dict = {}
for i in range(len(tables)):
    items = tables[i].find_all('td')
    print("size of items : ", len(items))

    step = 8
    if i == 3 or i == 5:
        step = 9

    for base_index in range(0, len(items), step):
        year_key = items[base_index].text.replace('\n', '')

        liibu = "吏部尚书"
        hubu = "户部尚书"
        libu = "礼部尚书"
        bingbu = "兵部尚书"
        xingbu = "刑部尚书"
        gongbu = "工部尚书"
        xxingbu = "行部尚书"
        yushi = "都御史"

        if i != 3 and i != 5:
            dict[year_key] = {  liibu:rename_arg(items[base_index + 1].text),
                                hubu:rename_arg(items[base_index + 2].text),
                                libu:rename_arg(items[base_index + 3].text),
                                bingbu:rename_arg(items[base_index + 4].text),
                                xingbu:rename_arg(items[base_index + 5].text),
                                gongbu:rename_arg(items[base_index + 6].text),
                                yushi:rename_arg(items[base_index + 7].text),
                            }
        else:
            dict[year_key] = {  liibu:rename_arg(items[base_index + 1].text),
                                hubu:rename_arg(items[base_index + 2].text),
                                libu:rename_arg(items[base_index + 3].text),
                                bingbu:rename_arg(items[base_index + 4].text),
                                xingbu:rename_arg(items[base_index + 5].text),
                                gongbu:rename_arg(items[base_index + 6].text),
                                xxingbu:rename_arg(items[base_index + 7].text),
                                yushi:rename_arg(items[base_index + 8].text),
                            }


# dict_json = json.dumps(dict, ensure_ascii=False)
with open('qiqing.json', 'w') as outfile:
    json.dump(dict, outfile, ensure_ascii=False)
