#!/usr/local/bin/python27
# -*- coding:utf-8 -*-
# 


import sys , os, math
sys.path.append("/home/yanai-lab/Sotsuken16/ege-t/www/simplejson/simplejson-2.5.2")
import simplejson as json
#import json
#path = "/export/space/araki-t/100img/"


filename = "tokucho.json"
jsonfile = open(filename, 'r') # Open the file.
list = json.load(jsonfile)  # Read the opened file as json.

imagelist = list.keys()

v1 = list[imagelist[0]]
kekka = []
for subtarget in imagelist:
    v2 = list[subtarget]
    x = 0
    total = 0
    for i in v1:
        print  float(v1[x]), float(v2[x]), float(v1[x])-float(v2[x])
        total += (float(v1[x])-float(v2[x]))**2
        x+=1
    print total,math.sqrt(total)
#    kekka[subtarget] = math.sqrt(total)
    kekka.append([math.sqrt(total),subtarget])


print "\n\n\n"
#for k, v in sorted(kekka.items, key=lambda a:a[1]):
for k, v in sorted(kekka):
    print k, v

