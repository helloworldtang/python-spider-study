#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'tangcheng'
__mtime__ = '9/22/2017'
"""

import urllib.request
import http.cookiejar
import urllib.parse

login_url = "http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=L768q"
post_data = urllib.parse.urlencode({
    "username": "weisuen",
    "password": "aA123456"
}).encode("utf-8")
req = urllib.request.Request(login_url, post_data)

req.add_header("User-Agent",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36")
# 使用http.cookiejar.CookieJar()创建CookieJar对象
cjar = http.cookiejar.CookieJar()
# 使用HTTPCookieProcessor创建cookie处理器，并以其为参数构建opener对象
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
# 将opener安装为全局
urllib.request.install_opener(opener)

file = opener.open(req)
data = file.read()
file = open("tmp/login.html", "wb")
file.write(data)
file.close()

index_url = "http://bbs.chinaunix.net"
index_data = urllib.request.urlopen(index_url).read()
f_handler = open("tmp/index.html", "wb")
f_handler.write(index_data)
f_handler.close()
