#! /usr/bin/env python

import sys
import textwrap

filename = sys.argv[1]
 
with open(filename) as f:
    content = f.readlines()

error = False
0

count = 0
verbatim = False
for line in content:
    count = count + 1
    found = "{verbatim}" in line or "{lstlisting}" in line
    if verbatim and found:
        verbatim = False
        continue
    elif not verbatim and found:
        verbatim = False
        continue
    elif '"' in line:
        print ("ERROR: found illegal quote in line", count)
        print ("      ", str(count) + ":", line)
        error = True
    if len(line) > 80:
        print ("WRNING: line longer than 80 characters")
        print ("      ", str(len(line)) + ":", line)

with open(filename) as f:
    content = f.read()


count_open = content.count("``")
count_closed = content.count("''")

if count_open != count_closed:
    sys.exit ("ERROR: quotes ``quoted text'' do not match")

        
if error:
    sys.exit("ERROR: illegal quote found")        
