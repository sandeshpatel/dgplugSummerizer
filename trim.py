#!/usr/bin/env python3
import re
import sys
import urllib.request

teacher = input("enter teacher's name (warning: case sensitive): ")
#open file to write summary
target = open("target.txt",'w')

#regular expression to find lines which are addressed to whole class
regular_expression = "^\[\d\d:\d\d\]\s<" + teacher + ">\s\S*[^:]\s"
regex=re.compile(regular_expression) 

#finding the lines which are matching the regular expression
log_url = sys.argv[1]
with  urllib.request.urlopen(log_url) as log:
	for line in log:
		#line in some byte form, decode to utf-8
		line = line.decode('utf-8')
		if re.match(regex, line ):
			print(line)
			target.write(line)

target.close()
