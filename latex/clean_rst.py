#!/usr/bin/python
import os
import sys
import fileinput



# Replace method 
def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text
 
# Dictionary with our find:replace values.
reps = {
	'\n\n ':'\n\n',
#	'sub':'dub'
}


f = open(sys.argv[1])
filedata = f.read()
f.close()

#newdata = filedata.replace("frame","cra")
newdata = replace_all(filedata,reps)

f = open(sys.argv[2],'w')
f.write(newdata)
f.close()
