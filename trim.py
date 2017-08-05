#!/usr/bin/env python3
"""
trim.py
=============
Copyright (C) 2017 by Sandesh Patel
====================================

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License version 3 as published by
the Free Software Foundation,

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


import sys
import urllib.request
from os import system

teacher = {"kushal","sayan"}
student = set() 

#checking if user has entered url
if len(sys.argv) < 2:
	print("FAILED \n run it by typing \n $ ./trim.py url_of_log ")
	exit() 

	
log_url = sys.argv[1]

print("\nPlease wait. Processing … \nOnce done, please press SPACE to scroll pagewise or q to quit. ")

#target file name = last token of url
target_file = log_url.split("/")[-1]

#open file to write summary
target = open(target_file,'w')

#finding set of students and teacher
with  urllib.request.urlopen(log_url) as log:
	for line in log:
		#line in some byte form, decode to utf-8
		line = line.decode('utf-8')
		words = line.split(" ")
		if len(words) <3:
			continue
		if words[2] == "next\n":
			teacher.add(words[1].strip("<>"))
		else:
			student.add(words[1].strip("<>"))
			

#finding the lines which are for whole class
with  urllib.request.urlopen(log_url) as log:
	for line in log:
		#line in some byte form, decode to utf-8
		line = line.decode('utf-8')
		words = line.split(" ")
		if len(words) < 3:
			continue
		if (words[1].strip("<>") in teacher) and (not ( words[2].strip(":,") in student)):
			target.write(line)

target.close()

#showing output with less command
system("less "+target_file)

print("\n"+"-"*20 + "log is logged to " +target_file+ "-"*20)
