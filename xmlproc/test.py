#!/usr/bin/python

from xml.parsers.xmlproc import xmlproc
import linecache
import collections
from operator import itemgetter
import sys, subprocess
TEST_TIMES = 0
LOG = open("dd_log.txt", 'w')
def test_one ( path ):
    global TEST_TIMES
    p = subprocess.Popen(["python", "xpcmd.py", path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    TEST_TIMES += 1
    out, err = p.communicate()
    if len(err) != 0:
        return "FAIL"
    return "PASS"
def build_temporary_test_file(charset):
    global LOG
    test_file_name = 'dd_test_tmp.xml'
    f = open(test_file_name, 'w+')
    for key, value in charset:
        f.write( value )
    f.seek(0)
    LOG.write(">>>>TEST CONTENT START<<<<\n")
    for line in f:
        LOG.write(line + "\n")
    LOG.write(">>>>>TEST CONTENT END<<<<<\n")
    f.close()
    return test_file_name
def get_file_content(path):
    with open(path, 'r') as f:
        content = f.read()
    f.close()
    return content
FAIL_CASE = ""
def test_set(char_set):
    global FAIL_CASE
    LOG.write("==============TEST START==============\n")
    if char_set == [] : 
        res = "PASS"
    else:
        fname = build_temporary_test_file( char_set )
        res = test_one ( fname )
        if res == "FAIL" :
            FAIL_CASE = get_file_content(fname)
    LOG.write("TEST RESULT : " + res + "\n")
    LOG.write("==============TEST END================\n")
    return res

