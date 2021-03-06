#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import socket
import numpy as np
import cgi, cgitb
import copy
import csv
import sys, os
from sys import argv
cgitb.enable()

hostname= "nboot2.cs.uec.ac.jp" # no need
#hostname= "gp06.cs.uec.ac.jp" # no need
host = "130.153.192.3" # nboot2
#host = "130.153.192.98" # gp06
port = 2410

#category = ["Ramen"] # Category directry in Original/ or Transferred/ 
#c = np.random.randint(0,len(category),1)[0]

me = "./realtimeenq.cgi"
imgdir = "./araki-t/Enquete/Original/" #%s/"%category[c]
orgdir = "/export/space/araki-t/Enquete/Original/" #%s/"%category[c]
transferred = "./araki-t/Enquete/Out/out.jpg"
#imglist = np.array(os.listdir(imgdir))
imglist = os.listdir(imgdir)
#imglist.remove("Out") #remove other file and directry from images list

rnum = np.random.randint(0, len(imglist)-1, 1)[0] #imglist[0-n-1] * 1 (out.jpg is number N)
img = "%s%s" % (imgdir,imglist[rnum])#[0])
orgdir_img = "%s%s" % (orgdir,imglist[rnum])#[0])

receive = cgi.FieldStorage()
good = receive.getvalue("better","none\n")
receive_styles = receive.getvalue("styles","none\n")
receive_weight = receive.getvalue("weight","none\n")
receive_image = receive.getvalue("image", "none")



###################
##styale-transfer##
n = 4 # number of styles
styles = np.random.randint(0,31,n)
percentage = ["0","0.25","0.5","0.75","1"]
weight = []
while n > 0:
    i =  np.random.randint(0,len(percentage),1)[0]
    weight.append(percentage[i])
    n -= 1
weight = ",".join(weight) #[0.25,1,0.5,0]
styles = ",".join(map(str, styles)) #[a,b,c,d] # style's numbers

try:
    pid = os.fork()
    if pid == 0:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))
        client.send("--style_index %s --style_weight %s %s" %(styles, weight, orgdir_img))
        response = client.recv(1024)
        sys.exit()
    os.wait()
except socket.error:
    # If daemon is dying, method in try: is missing.
    weight = '\n<h2 class="error">! DAEMON ERROR</h2><p class="error">Transfering daemon is dying now. She is "~/Style32/generatedaemon.py" Please wake her up in "nboot2" server!</p>'
################
##//translated##
################


head='''Content-type: text/html; charset=UTF-8\n\n
<!DOCTYPE html>
<head>
<title>Realtime transfer</title>
<link rel="stylesheet" type="type/css" href="">
<style type="text/css">
div.box {width: 100%; display: inline-table;}
div.box:after {content: "."; display: block; height: 0; clear: both; visibility: hidden;}

div.box div {border:solid #CEF 3px; border-radius:0.5em;}
div div.org {width:44%; float:left;}
div div.arr {width:44%; float:left; margin-left:0.5em;}
div.org input, div.arr input {width:90%; padding:5%;}
h2.error {border-left:0.5em #F99 solid; border-bottom:0.1em #F99 solid;}
.error {color:red;}
</style>
</head>
<body>
'''

body = '<h1>Show Realtime random transferred Img</h1>\n<p><a href="./index.cgi">home</a></p><p>choose most delicious one.</p>\n'
body += 'img:%s, styles:%s, weight:%s' % (imglist[rnum],styles,weight)

body += '\n<div class="box">'
body += '''\n<div class="org">\n<form method="POST" action="%s"><input type="image" src="%s"><input type="hidden" name="better" value="0"><input type="hidden" name="styles" value="%s"><input type="hidden" name="weight" value="%s">
</form></div>''' %(me, img, styles, weight)
body += '''\n<div class="arr">\n<form method="POST" action="%s"><input type="image" src="%s"><input type="hidden" name="better" value="1"><input type="hidden" name="styles" value="%s"><input type="hidden" name="weight" value="%s"><input type="hidden" name="image" value="%s">
</form></div>\n</div> \n''' %(me, transferred, styles, weight, imglist[rnum])

body += good + receive_styles + receive_weight + receive_image

feet= '''
</body>
</html>
'''

print head, body, feet
