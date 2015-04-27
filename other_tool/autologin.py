#! /usr/sbin/python env
# -*- coding:utf-8 -*-

'''
Created on PyCharm  

@author: Edison

@date: 15/4/27  下午3:09

@summary: 

@note: 

@version: 
'''
__author__ = 'Edison'

import urllib2
import cookielib

def auto_check():

    cj = cookielib.LWPCookieJar()

    cookie_support = urllib2.HTTPCookieProcessor(cj)

    opener = urllib2.build_opener(cookie_support)

    opener.addheaders = [
        ('User-Agent', 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36')
    ]

    # data = opener.open('http://www.smzdm.com/user/login')

    response = opener.open('http://www.baidu.com')

    for i in cookie_support:
        print str(i.name)

if __name__ == '__main__':
    auto_check()