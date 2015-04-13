#!/usr/bin/env python
# $Id: ddmin.py,v 2.2 2005/05/12 22:01:18 zeller Exp $
from functools import partial
import sys,getopt
from split import split
from listsets import listminus
#from test import *
from build_test_db import *
#import re
import test as Test
import os

PASS       = "PASS"
FAIL       = "FAIL"
UNRESOLVED = "UNRESOLVED"

def ddmin(circumstances, test):
    """Return a sublist of CIRCUMSTANCES that is a relevant configuration
       with respect to TEST."""
    
    assert test([]) == PASS
    assert test(circumstances) == FAIL

    n = 2
    while len(circumstances) >= 2:
        subsets = split(circumstances, n)
        assert len(subsets) == n

        some_complement_is_failing = 0
        for subset in subsets:
            complement = listminus(circumstances, subset)

            if test(complement) == FAIL:
                circumstances = complement
                n = max(n - 1, 2)
                some_complement_is_failing = 1
                break

        if not some_complement_is_failing:
            if n == len(circumstances):
                break
            n = min(n * 2, len(circumstances))

    return circumstances



try:
    (options,sysids)=getopt.getopt(sys.argv[1:],'')
except getopt.error,e:
    print "Usage error: "+e
    print "please give input"
    sys.exit(1)
ddmin(build_db(sysids[0]), Test.test_set)
print "simplify input : "
print Test.FAIL_CASE
print "total test times : ", Test.TEST_TIMES
Test.LOG.close()
os.remove('dd_test_tmp.xml')
