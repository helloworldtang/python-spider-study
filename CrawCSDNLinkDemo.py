#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'tangcheng'
__mtime__ = '9/21/2017'
"""
import re
import urllib.request


def getLink(url):
    print(url)
    # 模拟浏览器的请求
    headers = ("User-Agent",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]

    # 将opener安装为全局
    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(url)
    data = str(file.read())

    print(data)

    # url regex
    # url_pattern = '(https?//[^\s)";]+\.(\w|/)*)'
    url_pattern = '[a-zA-Z]+://[^\s]*[.com|.cn]'

    link = re.compile(url_pattern).findall(data)
    # 去除重复
    link = list(set(link))
    return link


# 入口Url
url = "http://blog.csdn.net"
# 获取对应网页中包含的链接地址
link_list = getLink(url)
for link in link_list:
    print("link", link)
