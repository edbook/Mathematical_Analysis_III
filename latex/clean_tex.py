#!/usr/bin/python
import re
import sys


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
    '\\begin{frame}': '\subsection',
    '\\end{frame}': '',
    '\\begin{block}': '\subsubsection',
    '\\end{block}': '',
    '\\begin{se}': '\subsubsection{Setning}',
    '\\end{se}': '',
    '\\begin{sex}': '\subsubsection{Setning}',
    '\\end{sex}': '',
    '\\begin{sk}': '\subsubsection{Skilgreining}',
    '\\end{sk}': '',
    '\\begin{sesk}': '\subsubsection{Setning og skilgreining}',
    '\\end{sesk}': '',
    '\\begin{hs}': '\subsubsection{Hjálparsetning}',
    '\\end{hs}': '',
    '\\begin{fs}': '\subsubsection{Fylgisetning}',
    '\\end{fs}': '',
    '\\begin{sy}': '\subsubsection{Sýnidæmi}',
    '\\end{sy}': '',
    '\\begin{fo}': '\subsubsection{Forrit}',
    '\\end{fo}': '',
    '\\begin{so}': '\subsubsection{Sönnun}',
    '\\end{so}': '',
    '\\begin{sotx}': '\subsubsection{Sönnun}',
    '\\end{sotx}': '',
    '\\æfing': '\section{Æfingardæmi}',
    '\\dæmi': '\subsubsection',
    '\\vfigura': 'MYND VANTAR HÉR!!!',
    '\\figura': 'MYND VANTAR HÉR!!!',
    re.compile(r'((?:\n\\.+)*)\\label\{(.*?)\}'): '\n\n.. _\\2:\n\\1',
    # re.compile(r'\\label\{(.*?)\}'): '.. _\\1: ',
    re.compile(r'\\ref\{(.*?)\}'): ':ref:`\\1`',
    # 'sub': 'dub'
}


f = open(sys.argv[1], encoding='utf8')
filedata = f.read()
f.close()

#newdata = filedata.replace("frame","cra")
#newdata = filedata.replace(filedata,reps)
lines = filedata.split('\n')
newdata = replace_all('\n'.join(lines), reps)



f = open(sys.argv[2], 'w')
f.write(newdata)
f.close()
