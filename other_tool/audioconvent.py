#! /usr/sbin/python env
# -*- coding:utf-8 -*-

'''
Created on PyCharm  

@author: Edison

@date: 15/3/19  下午2:07

@summary: 

@note: 

@version: 
'''
__author__ = 'Edison'

import os
import sys
import subprocess
import Queue
import threading

q = Queue.Queue(0)
NUM_WORKERS = 4

def convent():
    global q
    while q.qsize() > 1:
        file_to = q.get().split(".")[0]
        child = subprocess.Popen("ffmpeg -i {ifs} {ofs}".format(ifs=q.get(), ofs=file_to + ".wav"), shell=True)
        child.wait()


def walkdir(dir):
    global q
    for root, dir, files in os.walk(dir):
        for f in files:
            q.put(os.path.join(root, f))

walkdir(sys.argv[1])
threads = []
for x in xrange(NUM_WORKERS):
    threads.append(threading.Thread(target=convent))
for t in threads:
    t.start()
for t in threads:
    t.join()