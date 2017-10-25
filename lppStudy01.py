#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'tangcheng'
__mtime__ = '10/17/2017'
"""
import os

for num in range(4):
    print(num)

movies = ['the holy grail', 1975, 'terry jones $ terry gilliam', 91, ['graham chapman',
                                                                      ['michael palin', 'john cleese', 'terry gilliam',
                                                                       'eric idle', 'terry jones']]]


def print_lol(the_list, level=0):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, level + 1)
        else:
            for tab_stop in range(level):
                print('\t', end='')
            print(each_item)


print_lol(movies, 0)

print_lol(movies, 2)

names = ['john', 'eric', ['cleese', 'idle'], 'michael', ['palin']]

print_lol(names, 0)

print_lol(names)

print_lol(names, 2)

print_lol(names, -9)

print("os.getcwd():", os.getcwd())

data = open('caeer.txt',encoding='utf-8')
print("data.readline():", data.readline(), end='')
print("================")
for line in data:
    print(line)

data.seek(0)
