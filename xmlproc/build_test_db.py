#!/usr/bin/python
def build_db(path):
    fo = open(path, 'r')
    m = [] 
    i = 1
    for line in fo.readlines():
        for char in line:
            m.append((i, char))
            i+=1
    fo.close()
    return m
"""
def build_db(path):
    fo = open(path, 'r')
    m = []
    i = 1
    for line in fo.readlines():
        m.append(i)
        i+=1
    fo.close()
    return m
"""
#print build_db("/home/john/software_debug/HW1.3/xmlproc/demo/urls.xml")
