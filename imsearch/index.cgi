#!/usr/local/bin/python27
# -*- coding:utf-8 -*-

#画像を更新したら,./Imgの中でln -s /export/spacs/araki-t/dir_name
#そして./gabor.pyを実行

import sys, os, math
sys.path.append("/home/yanai-lab/Sotsuken16/ege-t/www/simplejson/simplejson-2.5.2")
import simplejson as json
# import json
import re
import cgi,cgitb
cgitb.enable()

jsondir = "./Json/"
defaultimg = "69.jpg"
defaultfile = "gabor"

myname = os.path.basename(__file__) # This file name.
menulist = [["Gabor","gabor"],["RGB color histogram","rgb"],["HSV color histogram","hsv"],["LUV color histogram","luv"],["DCNN","dcnn"]]
shuhoumenu = ["Euclidean", "Histogram"]

###########
##--CGI--##
###########

form = cgi.FieldStorage()
choosed = form.getvalue("images", defaultimg)
jsonname = form.getvalue("tokuchofile", defaultfile)
gridname = form.getvalue("tokuchogrid", "2")
shuhou = form.getvalue("shuhou",shuhoumenu[0])
h1 = shuhou+" by "+jsonname+gridname+"x"+gridname
###########
###########

filename = jsondir+jsonname+gridname*2+".json"
if jsonname == menulist[4][1]:
    filename = jsondir+jsonname+".json"
    h1 = shuhou+" by "+jsonname

jsonfile = open(filename, 'r') # Open the file.
list = json.load(jsonfile)  # Read the opened file as json.
imagelist = list.keys()
imgpath = "./Img/100img/"


v1 = list[imgpath+choosed]
kekka = [] ## kekka =["score", "imgURL"]
def kyoriselect(EorH):
    keisan = []  ## keisan =["score", "imgURL"]
    ######################
    ####--Euclidean--#####
    ######################
    if EorH == shuhoumenu[0]:
        for subtarget in imagelist:
            v2 = list[subtarget]
            total = 0
            for i in range(0,len(v1)): # [0]~[num of v1's culumn]
                h1, h2 = float(v1[i]), float(v2[i])
                total += math.sqrt((h1-h2)**2)

            #    kekka[subtarget] = math.sqrt(total)
            keisan.append([total, subtarget])

    ######################
    ####--histogram--#####
    #####--intersec--#####
    ######################
    elif EorH == shuhoumenu[1]:
        for subtarget in imagelist:
            v2 = list[subtarget]
            total = 0
            for i in range(0,len(v1)): # [0]~[num of v1's culumn]
                # "math.favs(X)" is the absolute value of X.
                h1, h2 = float(v1[i]), float(v2[i])
                total += (h1+h2-math.fabs(h1-h2))/2
            keisan.append([total,subtarget])
    
    return keisan

#####-*--*--*--*-#####
##--kyoriselect end-##
######################

kekka = kyoriselect(shuhou)




#####################
######---menu---#####
#####################

menu = '''<form method="POST" action="%s">
<input type="hidden" name="images" value="%s">\n''' % (myname,choosed)
fileselect = '''<select name="tokuchofile">\n'''
grid = '''<select name="tokuchogrid">\n'''
tokuchouselect = '''<select name="shuhou">\n'''

for k in menulist:
    fileselect += '''<option value="%s">%s</option>\n''' % (k[1],k[0])
for l in range(1,4):
    grid += '''<option value="%d">%dx%d</option>\n''' % (l,l,l)
for m in shuhoumenu:
    tokuchouselect += '''<option value="%s">%s</option>\n''' % (m, m)

fileselect += '''</select>\n'''
grid += '''</select>\n'''
tokuchouselect += '''</select>\n'''
menu += tokuchouselect+fileselect+grid+'''<input type="submit" value="go"></form>'''






######################
###--table making--###
#####--and sort--#####
######################
culumn = 10 #カラムの個数
current = 0 
table = '''<table>\n'''



def maketable(score, fname, count):
    karitable = ""
    if count % culumn == 0:
        karitable += "<tr>\n"

    karitable+='''<td><form method="POST" action="%s"><input type="hidden" name="images" value="%s"><input type="hidden" name="tokuchofile" value="%s"><input type="hidden" name="tokuchogrid" value="%s"><input type="hidden" name="shuhou" value="%s"><input type="image" src="%s"></form>%f</td>\n''' %(myname, os.path.basename(fname), jsonname, gridname, shuhou, imgpath+os.path.basename(fname), score)


    return karitable
######################
######################

if shuhou == shuhoumenu[0]:
    for kyori, filename in sorted(kekka):
        table += maketable(kyori, filename, current)
        current += 1
        if current % culumn == 0:
            table += "</tr>\n"
elif shuhou == shuhoumenu[1]:
    for kyori, filename in sorted(kekka, reverse=True):
        table += maketable(kyori, filename, current)
        current += 1
        if current % culumn == 0:
            table += "</tr>\n"

table += "</table>"

######################
######################


text='''Content-type: text/html; charset=UTF-8\n\n
<!DOCTYPE html>
<head>
<title>Image Search by GABOR with Histogram Intersection</title>
<link rel="stylesheet" type="type/css" href="">
<style type="text/css">
<!--
img {width:10em;}
input {width:7em;}
h1 {border-left:navy 0.3em solid; border-bottom:navy dashed 0.1em;
    padding: 0 0 0.5em 0.5em;
}

body {background:#CFF; padding-left:2%; border-bottom:navy dashed 0.1em;
      padding-bottom:10%;
}
-->
</style>
</head>
<body>
'''
text += '''<h1>%s</h1>''' % (h1)
text += '''<p><a href="http://mm.cs.uec.ac.jp/araki-t/">araki-t</a></p>'''

text += menu
text += '''<img src="%s" alt="%s">''' % (imgpath+choosed,choosed)
text += table



text += '</body></html>'
print text
