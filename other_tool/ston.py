#! /usr/sbin/python env
# -*- coding:utf-8 -*-

'''
Created on PyCharm  

@author: Edison

@date: 15/4/1  下午1:42

@summary: 

@note: 

@version: 
'''
__author__ = 'Edison'

import random

guess_list = ['石头', '剪刀', '布']

win_combination = [['石头','剪刀'], ['布','石头'], ['剪刀','布']]

while True:
    computer = random.choice(guess_list)
    people = raw_input('张萌萌大战铁血战士 -- 请请出招: 剪刀, 石头, 布\n').strip()
    if people not in guess_list:
        people = raw_input('请按照套路出招: 剪刀, 石头, 布\n').strip()
        continue
    print "铁血战士: " + computer
    if computer == people:
        print "\xe2\x9e\x9c 平手"
    elif [computer, people] in win_combination:
        print "\xe2\x9e\x9c 铁血战士胜"
    else:
        print "\xe2\x9e\x9c 张萌萌胜"
        continue