#!/usr/bin/python
import re
import os
import sys
import fileinput



# Replace method 
def replace_all(text, dic):
    for i, j in dic.items():
        if type(i) == str:
            text = text.replace(i, j)
        else:
            text = i.sub(j, text)
    return text
 
# Dictionary with our find:replace values.
reps = {
	'\n\n ':'\n\n',
	'.. \\_': '.. _',
    re.compile(r'\n\s+.. _'): '\n.. _',
    #re.compile(r':ref:‘(.*?)‘'): ':ref:`\\1`',
    re.compile(r':ref:‘(.*?)‘'): ':ref:`Link title <\\1>`',
#	'sub':'dub'
}


f = open(sys.argv[1])
filedata = f.read()
f.close()

#newdata = filedata.replace("frame","cra")
#newdata = replace_all(filedata,reps)
lines = filedata.split('\n')
newdata = replace_all('\n'.join(lines[11:]), reps)

f = open(sys.argv[2],'w')
f.write(newdata)
f.close()
