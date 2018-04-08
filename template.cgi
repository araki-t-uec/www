#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import cgi
import cgitb
import copy
import csv
import sys
cgitb.enable()

head='''Content-type: text/html; charset=UTF-8\n\n
<!DOCTYPE html>
<head>
<title></title>
<link rel="stylesheet" type="type/css" href="">
</head>
<body>'''

body='''
<h1>hello world</h1>
'''

feet= '''
</body>
</html>
'''

print head, body, feet
