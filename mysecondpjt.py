#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'tangcheng'
__mtime__ = '12/12/2017'
"""

import re
from urllib import request
from urllib import parse
from urllib.request import urlopen


def getHtml(url):
    page = urlopen(url)
    html = page.read()
    return html


def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    html = html.decode('utf-8')
    imglist = re.findall(imgre, html)
    x = 0
    for imgurl in imglist:
        request.urlretrieve(imgurl, '%s.jpg' % x)
        x = x + 1


html = getHtml("http://tieba.baidu.com/p/2460150866")
print(getImg(html))