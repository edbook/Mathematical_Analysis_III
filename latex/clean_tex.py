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

    # For labels and references:
    re.compile(r'((?:\n\\.+)*)\\label\{(.*?)\}'): '\n\n.. _\\2:\n\\1',
    re.compile(r'\\ref\{(.*?)\}'): ':ref:`\\1`',
    # re.compile(r'\\label\{(.*?)\}'): '.. _\\1: ',

    # For pictures:
    '\\begin{picture}': 'MYND VANTAR HÉR!!!\n\\begin{picture}',
    #'\\vfigura': 'MYND VANTAR HÉR!!!',
    #'\\figura': 'MYND VANTAR HÉR!!!',
    re.compile(r'\\v?figura ?\{(.*?)\}\{\{.*?Mynd: (.*?)\}\}'): '.. figure:: ./myndir/\\1.svg\n    :align: center\n\n    Mynd: \\2\n\n',
    re.compile(r'\\v?figura ?\{(.*?)\}\{(.*?)\}'): '.. figure:: ./myndir/\\1.svg\n    :align: center\n\n    \\2\n\n',

    # For indexing: (NOTE: MANUAL WORK STILL NEEDED! This just helps out!)
    re.compile(r'\\index\{(.*?)\}'): ':hover:`\\1`',
    # 'sub': 'dub'
}


f = open(sys.argv[1], encoding='utf8')
filedata = f.read()
f.close()

#newdata = filedata.replace("frame","cra")
#newdata = filedata.replace(filedata,reps)
lines = filedata.split('\n')
newdata = replace_all('\n'.join(lines), reps)


working_data = list(newdata)
length_of_opening_tag = len('\set{')
length_of_closing_tag = len('}')
maximum_index = len(working_data) - length_of_opening_tag - length_of_closing_tag
index = 0
depth = 0
while index < maximum_index:
    if working_data[index:index+length_of_opening_tag] == list('\set{'):
    #print(working_data[index:index+length_of_opening_tag], "found!")
        del working_data[index+1:index+4]
        maximum_index -= 3
        index += 2
        depth = 1
        while depth > 0:
            if working_data[index] == '{':
                depth += 1
            if working_data[index] == '}':
                depth -= 1
            index += 1
        working_data.insert(index-1, '\\')
        maximum_index += 1
        index += 1
    index += 1


f = open(sys.argv[2], 'w')
f.write(''.join(working_data))
f.close()
