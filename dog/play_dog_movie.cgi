#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import cgi
import cgitb
import copy
import csv
import sys,os
cgitb.enable()
myname = os.path.basename(__file__) # This file name.
html_form_text = '''<form method="POST" action="./%s">\n'''%myname
dogs_list = ["Hime", "Ku", "Ringo", "Ryu"]
tags_list = ["Car","Drink","Feed","Look_at_Left","Look_at_Right","Pet","Play_with_ball","Shake","Sniff","Trun_Right","Walk"]

default_dog = "Hime"
default_tag = "Car"
giflist_org = [] # gitfile_url & tags
giflist = [] # output to html giflist
mnt = []

f = open('./gifpathtext_withtag')
giftext = f.read()
f.close

for i in giftext.split("\n"):
    giffile = i.split(",")
    giflist_org.append(giffile)


# HEAD

head='''Content-type: text/html; charset=UTF-8\n\n
<!DOCTYPE html>
<head>
<title>play dog.avi</title>
<link rel="stylesheet" type="type/css" href="">
</head>
<body>
'''


## FORM
form = cgi.FieldStorage()
dog_name = form.getvalue("dog", default_dog)
tag_name = form.getvalue("tags", default_tag)
dogtag_title = dog_name + "_" + tag_name

# to make show_file_list ( giflist ) 
for i in giflist_org:
    try:
        if i[1] == dog_name:
            mnt.append(i)
    except:
        pass

for i in mnt:
    if i[2] == tag_name:
        giflist.append(i)

html_form_text += '<select name="dog">\n'
for i in dogs_list:
    html_form_text += '''<option value="%s">%s</option>\n'''%(i,i)
html_form_text += '</select>\n<select name="tags">\n'
for i in tags_list:
    html_form_text += '''<option value="%s">%s</option>\n'''%(i,i)
html_form_text += '</select>\n<input type="submit"></form>\n'



## BODY

body='''
<h1>Play dog movie dataset</h1>
%s
<h2>%s</h2>
<p><a href="./index.cgi">home</a></p>
'''%(html_form_text, dogtag_title)

imglist = ""
for i in giflist:
    imglist +="<img src=\"%s\">\n"%i[0]

feet= '''</body>
</html>
'''

print head, body, imglist, feet
