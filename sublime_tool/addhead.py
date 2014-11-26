#! -*- coding : utf-8 -*- 

#/usr/bin/env python


'''
Created on 2013-12-26 18:16:26

@author: Edison

@summary: 

@version: V1.0

@bug:

@note:
'''


import sublime, sublime_plugin
from datetime import *
import time

class addheadCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        text_py = '''# -*- coding:utf-8 -*- 

#! /usr/bin/env python


\'\'\'
Created on %s

@author: Edison

@summary: 

@version: V1.0

@bug:

@note:
\'\'\'
\n
'''
        text_php = '''<?php

/**
*   Created on %s
*/

header("Content-Type: text/html; charset=utf-8");

class 
?>
''' 
    
        text_js = '''/**
    Created on %s

    @author: Edison

    @summary: 

    @version: V1.0

    @bug:

    @note:
*/
'''

        nowtime = datetime.now().strftime('%Y-%m-%d %X');
        filename = self.view.file_name()
        _name    = filename.split(".")[-1]          
        _dict    = {
            "php" : text_php %(nowtime),
            "py"  : text_py  %(nowtime),
            "js"  : text_js  %(nowtime)
        }
        
        self.view.insert(edit, 0, _dict[_name])

