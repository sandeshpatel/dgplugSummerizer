#!/usr/bin/env python3
import re
import sys
import urllib.request
from os import system

teacher = {"kushal","sayan"}
print("logs will be saved to %s " %("target.txt"))
#open file to write summary
target = open("target.txt",'w')


#finding the lines which are matching the regular expression
log_url = sys.argv[1]
with  urllib.request.urlopen(log_url) as log:
	for line in log:
		#line in some byte form, decode to utf-8
		line = line.decode('utf-8')
		words = line.split(" ")
		if len(words) <3:
			continue
		if words[2] == "next\n":
			teacher.add(words[1].strip("<>"))
			


with  urllib.request.urlopen(log_url) as log:
	for line in log:
		#line in some byte form, decode to utf-8
		line = line.decode('utf-8')
		words = line.split(" ")
		if len(words) < 3:
			continue
		if (words[1].strip("<>") in teacher) and( not words[2].endswith(":")):
			target.write(line)

target.close()

system("less "+"target.txt")
