#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3, random
import numpy as np
import cgi, cgitb
import copy
import csv
import sys, os
from sys import argv
cgitb.enable()

#category = ["Ramen"] # Category directry in Original/ or Transferred/ 
#c = np.random.randint(0,len(category),1)[0]

me = "./enq.cgi"
dbfile = "./Data/enq_db_201804"
imgdir = "./araki-t/Enquete/Ramen/Original/" #%s/"%category[c]
#transferred = "./araki-t/Enquete/Transferred/" #%s/"%category[c]
orgdir = "/export/space/araki-t/Enquete/Ramen/Original/" #%s"%category[c]
#imglist = np.array(os.listdir(imgdir))
imglist = os.listdir(imgdir)
#imglist.remove("Out") #remove other file and directry from images list

rnum = np.random.randint(0, len(imglist)-2100, 1)[0] #imglist[0-n-1] * 1 (out.jpg is number N)
img = "%s%s" % (imgdir,imglist[rnum])
orgdir_img = "%s%s" % (orgdir,imglist[rnum])

receive = cgi.FieldStorage()
good = receive.getvalue("better",0)
receive_image = receive.getvalue("image", "no.jpg")

#################
###UPdate Sqlite###
#################
table = sqlite3.connect(dbfile)
exc = table.cursor()
num_of_dir = 20
selecting = True
#score = np.array([0]*num_of_dir)
#exit()
score=0
try:
    #Check The table has receive_image data.
    command = 'SELECT "%s" FROM weights where imagename="%s";'%(good, receive_image)
    items = exc.execute(command)
    score = items.fetchall()[0][0]
    selecting = False
except IndexError:
    score = 0
except Exception:
    print "Exception"
    #If There are not tha table, create it. 
    table.execute('CREATE TABLE weights(imagename, "0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19", category);')

if selecting:
    # There are no score when the table have not the receive img data. 
    table.execute('INSERT INTO weights VALUES(?, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, "ramen");',[receive_image])

#Add received figure to it then Score is Zero or more.
command = '''UPDATE weights set "%s"=%s where imagename="%s"''' % (good, score+1, receive_image)
exc.execute(command)

table.commit()
exc.close()
###################
###################

###################
# POST LIST #
transed_number = range(0, 20)
random.shuffle(transed_number)

postlist = '''<div class="box">\n''' 
for i in transed_number:
    if i == 0:
        postlist += '''<div class="arr"><form method="POST" action="%s"><input type="image" src="%s" name="image"><input type="hidden" name="better" value=0><input type="hidden" name="image" value="%s"></form></div>\n''' % (me, imgdir+imglist[rnum], imglist[rnum])
    else :
        postlist += '''<div class="arr"><form method="POST" action="%s"><input type="image" src="./araki-t/Enquete/Ramen/Transferred_%d/%s" name="image"><input type="hidden" name="better" value=%d><input type="hidden" name="image" value="%s"></form></div>\n''' % (me, i, imglist[rnum], i, imglist[rnum])

postlist += "</div>"
###################
###################



head='''Content-type: text/html; charset=UTF-8\n\n
<!DOCTYPE html>
<head>
<title>RAND IMG</title>
<link rel="stylesheet" type="type/css" href="">
<style type="text/css">
div.box {width: 100%; display: inline-table;}
div.box:after {content: "."; display: block; height: 0; clear: both; visibility: hidden;}

div.box div {border:solid #CEF 3px; border-radius:0.5em;}
div div.arr {width:15%; float:left; margin-left:0.5em;}
div.org input, div.arr input {width:90%; padding:5%;}
h2.error {border-left:0.5em #F99 solid; border-bottom:0.1em #F99 solid;}
.error {color:red;}
</style>
</head>
<body>
'''

body = '<h1>choose most delicious one.</h1>\n<ul><li><a href="./index.cgi">index</a></li><li><a href="http://mm.cs.uec.ac.jp/araki-t/">home</a></li></ul><p></p>\n'
body += '\n<br>img:%s' % (imglist[rnum])
body += postlist

body += "received data:" + str(good) + receive_image
feet= '''
</body>
</html>
'''

print head, body, feet
