#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'tangcheng'
__mtime__ = '9/20/2017'
"""
import re
import urllib.request
import urllib.error
import os.path


def craw(url, page):
    html_data = urllib.request.urlopen(url).read()
    html_data = str(html_data)

    pattern_container_div = '<div id="plist".+? <div class="page clearfix">'
    result = re.compile(pattern_container_div).findall(html_data)
    result = result[0]

    print("result:", result)

    pattern_data_img = '<img width="220" height="220" data-img="1" src="//(.+?\.jpg)"'
    image_list = re.compile(pattern_data_img).findall(result)

    print("image_list:", image_list)

    x = 1
    for image_url in image_list:
        # print("x:", x)
        # print(image_url)
        basename = os.path.basename(image_url)
        print(basename)
        image_name = "images/" + str(page) + str(x) + basename
        image_url = "http://" + image_url

        try:
            urllib.request.urlretrieve(image_url, filename=image_name)
            x += 1
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                x += 1
            if hasattr(e, "reason"):
                x += 1
            print(e)


for i in range(1, 10):
    url = "http://list.jd.com/list.html?cat=9987,653,655&page=" + str(i) + "&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main"
    print(url)
    craw(url, i)
