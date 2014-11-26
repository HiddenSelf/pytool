#! -*- coding : utf-8 -*- 

#/usr/bin/env python


'''
Created on 2013-12-26 18:16:41

@author: Edison

@summary: 

@version: V1.0

@bug:

@note:
'''


import sublime, sublime_plugin
import time
from datetime import *


class addannotationCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		zhushi_php = '''

	/**
	*	@cc %s -*- 
	*/	
'''
		
		zhushi_python = '''
#-- 
#   @time: %s -*- 
#	@summary: 
#--
'''
		for region in self.view.sel():			
			nowtime  = datetime.now().strftime('%Y-%m-%d %X');
			filename = self.view.file_name()
			_name    = filename.split(".")[-1]			
			_dict    = {
				"php" : zhushi_php %(nowtime),
				"py"  : zhushi_python %(nowtime)
			}		
			if region.empty():				
				line = self.view.line(region)
				# line_contents = self.view.substr(line) + '\n'
				self.view.insert(edit, line.begin() ,_dict[_name].strip())
			else:
				self.view.insert(edit, region.begin(), self.view.substr(region))				
				self.view.insert(edit, line.begin(),_dict[_name]) 

