#!/usr/bin/python
# -*- coding:utf-8 -*-

# path中のimg画像から特徴量を抽出してハッシュでtokucho.txtに格納します


import commands, os, imghdr, shutil, json, re, sys
#path = "/export/space/araki-t/100img/"
path = "./Img/100img/"
filedir = "./Json/"
tokucho = {}
menu = ["gabor","rgb","hsv","luv"]
argvs = sys.argv
argc = len(argvs)

if argc < 3:
    print "%s (-f[0-4]) [1-3]" % __file__
    print "  -f\t0: Gabor (default) \n\t1: RGB color histogram \n\t2: HSV color histogram \n\t3: Luv color histogram \n\t4: DCNN"
    print "exam:\t%s 0 1" % __file__
    quit()
elif int(argvs[1]) > 4 or int(argvs[1]) < 0:
    print "argv[1] is worng"
    quit()
elif int(argvs[2]) > 3 or int(argvs[2]) < 1:
    print "argv[2] is worng"
    quit()
else:
    filename = filedir+menu[int(argvs[1])]+argvs[2]*2+".json"
    mode = argvs[1]
    grid = argvs[2] + " " + argvs[2]


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
    gabor = commands.getoutput("~yanai/Pub/im/gabor/gabor -f %s %s %s" % (mode, file, grid))
    data = gabor.split() #空白文字を区切りに分割
    clum = []
    count = 0
    for i in data:
        x = int(i.split(":")[0])-1
        if x != count:
            while count < x:
                clum.append("0.0")
                count += 1
        #    clum.append(i.split(":")[1])
        clum.append(count)  #malloc代わり
        clum[x]=i.split(":")[1]
        count+=1

    tokucho[file] = clum


#gabor = commands.getoutput("~yanai/Pub/im/gabor/gabor ./Img/100img/3.jpg 2 2")


print tokucho
print "\tmode -f:\t%s\n \tgrid:\t%s" %(mode,grid)

with open(filename, 'w') as f:
    json.dump(tokucho, f)
