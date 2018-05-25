#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import cgi
import cgitb
import copy
import csv
import sys
cgitb.enable()


#HEAD

head='''Content-type: text/html; charset=UTF-8\n\n
<!DOCTYPE html>
<head>
<title>play dog.avi</title>
<link rel="stylesheet" type="type/css" href="">
</head>
<body>
'''


##BODY

body='''
<h1>Play dog movie dataset</h1>
<p><a href="./index.cgi">home</a></p>
<video src="http://mm.cs.uec.ac.jp/araki-t/araki-t/robotics-ftp.ait.kyushu-u.ac.jp/dogcentric/Ryu/Walk/Walk_Ryu_2_3700_3825.mp4">
Your browser is not supported video tags (html5).
</video>
-----
'''

feet= '''
</body>
</html>
'''

print head, body, feet
