#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import cgi, cgitb
import copy
import csv
import sys, os
cgitb.enable()

pid = os.fork()
if pid == 0:
    print 'chiled process'
    sys.exit()

head='''Content-type: text/html; charset=UTF-8\n\n
<!DOCTYPE html>
<head>
<title></title>
<link rel="stylesheet" type="type/css" href="">
</head>
<body>'''

body='''
<h1>Fork Exec</h1>
'''

feet= '''
</body>
</html>
'''

print head, body, feet
