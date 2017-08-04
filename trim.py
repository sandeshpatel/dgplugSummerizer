#!/usr/bin/env python3
import re
import sys
import urllib.request
from os import system

teacher = {"kushal","sayan"}
student = set() 
#open file to write summary
log_url = sys.argv[1]
target_file = log_url.split("/")[-1]
print("\n"+"-"*20 + "logs will be saved to " +target_file+ "-"*20)
target = open(target_file,'w')


#finding the lines which are matching the regular expression
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

system("less "+target_file)
