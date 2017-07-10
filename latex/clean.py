#!/usr/bin/python
import os
import sys
import fileinput



# Replace method 
def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text
 
# Dictionary with our find:replace values.
reps = {
	'\\begin{frame}':'\subsection', 
	'\\end{frame}':'',
	'\\begin{block}':'\subsubsection', 
	'\\end{block}':'',
	'\\begin{theorem}':'\subsubsection', 
	'\\end{theorem}':'',
	'\\begin{definition}':'\subsubsection', 
	'\\end{definition}':'',
	'\\begin{proof}':'\subsubsection', 
	'\\end{proof}':'',
	'\\begin{proposition}':'\subsubsection', 
	'\\end{proposition}':'',
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
