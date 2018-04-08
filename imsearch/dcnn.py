#!/usr/bin/python
# -*- coding:utf-8 -*-

# path中のimg画像から特徴量を抽出してハッシュでtokucho.txtに格納します


import commands, os, imghdr, shutil, json, re, sys
path = "./Img/100img/"
filedir = "./Json/"
tokucho = {}
menu = ["dcnn"]


filename = filedir+menu[0]+".json"

def get_image_list(path):
    file_list = []
    for (root, dirs, files) in os.walk(path): # 再帰的に探索
        for file in files: # ファイル名だけ取得
            target = os.path.join(root,file).replace("\\", "/")  # フルパス取得
            if os.path.isfile(target): # ファイルかどうか判別
                if imghdr.what(target) != None : # 画像ファイルかどうかの判別
                    file_list.append(target) # 画像ファイルであればリストに追加
    return file_list

list = get_image_list(path)


for file in list:
    deepc = commands.getoutput("~yanai/Pub/deeplearning/overfeat/bin/linux_64/overfeat -f %s | ~yanai/Pub/deeplearning/overfeat/l2_norm" % (file))
    data = deepc.split() #空白文字を区切りに分割
    clum = []
    count = 0

#    print data,file
    tokucho[file] = data

#print tokucho
print filename
with open(filename, 'w') as f:
    json.dump(tokucho, f)
