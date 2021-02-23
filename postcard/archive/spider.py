#!/usr/bin/env python3.9

from typing import Any
import requests
from lxml import etree

url = "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2020/index.html" # 爬虫真的爬到国家统计局了（没有 https 真的菜
res = {}

# @Xecades 2020 年暑假前夕为我写的代码
def getText(url: str) -> str:
    headers = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
        'Accept-Language': r'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    }
    response = requests.get(url, headers=headers)
    return response

def parseProv(content: str) -> Any:
    xml = etree.HTML(content)

prov = getText(url)
prov

("/html/body/table[2]/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[@class='provincetr']/td")
