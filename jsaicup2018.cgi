#!/usr/bin/python
# -*- coding:utf-8 -*-

import cgi, cgitb
import os, sys, csv
masterfile = file("./araki-t/Deepanalytics/Jsaicup2018/master.tsv")
mastertablefile = file("./araki-t/Deepanalytics/Jsaicup2018/train_master.tsv")
masterdata = csv.reader(masterfile, delimiter = '\t')
mastertable = csv.reader(mastertablefile, delimiter = '\t')
imagedir = "./araki-t/Deepanalytics/Jsaicup2018/train_image/"
me="jsaicup2018.cgi"

form = cgi.FieldStorage()
category_int = form.getvalue("category", "0")

index='''Content-type: text/html; charset=UTF-8\n\n
<!DOCTYPE html><head>
<style type="text/css">
<!--
body {width:100%;}
div.menu {float:left; border:solid navy 1px; width:10%;}
table {width:80%;}
td {width:3%;}
img {width:100%;}
-->
</style>
</head><body>'''

index +='''<div class="menu"><a href="http://mm.cs.uec.ac.jp/araki-t/jsaicup2018test.cgi">testimage</a>\n'''
formtext = '''<form methot="POST" action="%s"><input type="hidden"  name="category" value="''' % (me)
for i in masterdata:
    index += '''%s%s"><input type="submit" value="%s"></form>\n''' % (formtext,i[1],i[0]+i[1])
index += "</div>"

n = 0
table = "<table>\n<tr>"
for i in mastertable:
    if i[1] == category_int:
        n+=1
        table += '''<td><a href="%s"><img src="%s%s" alt="%s"></a><br>%s</td>''' % (imagedir+i[0], imagedir, i[0],i[0], i[0])
        if n%10 == 0:
            table += "</tr>\n<tr>"

table += "</tr></table>\n"

index += '''<p>[category num: %s], [num of img: %d], [imgdir: "%s"]</p>'''%(category_int, n, imagedir)

index += table
index += "</body></html>"

print index
