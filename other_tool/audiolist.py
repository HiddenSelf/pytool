#! /usr/sbin/python env
# -*- coding:utf-8 -*-

'''
Created on PyCharm  

@author: Edison

@date: 14/11/26  上午11:32

@summary: 

@note: 

@version: 
'''
__author__ = 'Edison'

import os
import random

path = "/Users/Edison/Music/Audios"

def crerandomaudiolist():
    _files = []
    for root, dir, files in os.walk(path):
        for f in files:
            _files.append(os.path.join(root, f+"\r\n"))

    print _files
    print len(_files)
    with open(os.path.join(path, "audio.list"), "ab") as of:
        for i in random.sample(range(0, len(_files)-1), len(_files)):
            of.write(_files[i])

## exec
crerandomaudiolist()

