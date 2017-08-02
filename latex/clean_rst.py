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
    '\\sp': '^',
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


italics_replacement_rules = {
    re.compile(r'^([^:][^m][^a][^t][^h][^:])'): r'*\1',
    re.compile(r'^:math:`(.*?)` '): r':math:`\1` *',
    re.compile(r'( :math:`.*?` )'): r'*\1*',
    re.compile(r'(?<!`)$'): r'*',
    re.compile(r' :math:`(.*?)`$'): r'* :math:`\1`',
}
    

split_by_star = newdata.split('*')
for index, _ in enumerate(split_by_star):
    if index % 2 == 1:
        split_by_star[index] = replace_all(split_by_star[index], italics_replacement_rules)

fixed_italics = ''.join(split_by_star)





f = open(sys.argv[2],'w')
f.write(fixed_italics)
f.close()
