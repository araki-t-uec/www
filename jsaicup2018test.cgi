#!/usr/bin/python
# -*- coding:utf-8 -*-

import cgi, cgitb
import os, sys, csv
masterfile = file("./araki-t/Deepanalytics/Jsaicup2018/master.tsv")
masterdata = csv.reader(masterfile, delimiter = '\t')
imagedir = "./araki-t/Deepanalytics/Jsaicup2018/test_image/"
me="jsaicup2018test.cgi"

form = cgi.FieldStorage()
page = form.getvalue("page", "0")

index='''Content-type: text/html; charset=UTF-8\n\n
<!DOCTYPE html><head>
<style type="text/css">
<!--
body {width:100%;}
div.menu {float:left; width:10%;}
table {width:80%;}
td {width:3%;}
img {width:100%;}
-->
</style>
</head><body>'''

index +='''<div class="menu"><a href="http://mm.cs.uec.ac.jp/araki-t/jsaicup2018.cgi">train_image</a>\n'''

for i in range(40):
    index += '''<form method="POST" action="%s"><input type="hidden" name ="page" value="%d"><input type="submit" value="%d"></form>'''%(me,i,i)
index+="</div>"


n=int(page)*100
table = "<table>\n<tr>"
for i in range(n, n+100):
        table += '''<td><a href="%stest_%s.jpg"><img src="%stest_%s.jpg" alt="%s"></a><br>%s</td>''' % (imagedir, i, imagedir, i, i, i)
        if i%10 == 9:
            table += "</tr>\n<tr>"

table += "</tr></table>\n"

index += '''<p>[imgdir: "%s"]</p>'''%(imagedir)

index += table
index += "</body></html>"

print index
