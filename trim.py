#!/usr/bin/env python3
import re

teacher = "sayan"
# opening file to read from 
file_name = "Logs-2017-07-31-13-33.txt"
log  = open(file_name, 'r')
#open file to write summary
target = open("target.txt",'w')

#regular expression to find lines which are addressed to whole class
regular_expression = "^\[\d\d:\d\d\]\s<" + teacher + ">\s\S*[^:]\s"
regex=re.compile(regular_expression) 

#finding the lines which are matching the regular expression
for line in log:
	if re.match(regex, line ):
		print(line)
		target.write(line)
