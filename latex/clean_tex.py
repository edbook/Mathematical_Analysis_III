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
	'\\begin{frame}':'\subsection', 
	'\\end{frame}':'',
	'\\begin{block}':'\subsubsection', 
	'\\end{block}':'',
	'\\begin{se}':'\subsubsection{Setning}',
	'\\end{se}':'',
	'\\begin{sex}':'\subsubsection{Setning}', 
	'\\end{sex}':'',
	'\\begin{sk}':'\subsubsection{Skilgreining}', 
	'\\end{sk}':'',
    '\\begin{sesk}':'\subsubsection{Setning og skilgreining}',
	'\\end{sesk}':'',
	'\\begin{hs}':'\subsubsection{Hjálparsetning}', 
	'\\end{hs}':'',
	'\\begin{fs}':'\subsubsection{Fylgisetning}', 
	'\\end{fs}':'',
	'\\begin{sy}':'\subsubsection{Sýnidæmi}', 
	'\\end{sy}':'',
	'\\begin{fo}':'\subsubsection{Forrit}', 
	'\\end{fo}':'',
	'\\begin{so}':'\subsubsection{Sönnun}', 
	'\\end{so}':'',
	'\\begin{sotx}':'\subsubsection{Sönnun}', 
	'\\end{sotx}':'',
	'\\æfing':'\section{Æfingardæmi}', 
	'\\dæmi':'\subsubsection',
	'\\vfigura':'MYND VANTAR HÉR!!!',
	'\\figura':'MYND VANTAR HÉR!!!',
    #r'\\label\{.*?\}':r'\.\. _\\1:',
	#'\\ref\{.*?\}':':ref:`\\1`',
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
