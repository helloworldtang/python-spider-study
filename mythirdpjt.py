#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'tangcheng'
__mtime__ = '12/12/2017'
"""

import urllib.request
import re

from db.DBUtil import persist


def getContent(url):
    headers = ("User-Agent",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)

    urlopen = urllib.request.urlopen(url)
    data = urlopen.read().decode("utf-8")
    # print(data)
    userpat = '<title>(.*?)<'
    titleList = re.compile(userpat, re.S).findall(data)
    print("titleList-->", titleList)
    for title in titleList:
        print("data:", title)
        persist(url,title)


if __name__ == '__main__':
    getContent("http://jd.com")
    getContent("http://chaojihao.net")
