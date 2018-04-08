#!/usr/bin/tcsh
# -*- coding:utf-8 -*-

set category="つけ麺" #food category 
set outfilename="tukementext" #outfile name
#set outfilename="testtext" #make seafty

set source="/export/space4/yanai/foodbot/log/201711.log" #foodbots log name
set output="/export/space/araki-t/Enquete/$outfilename" #output dir name

#nkf -u /export/space4/yanai/foodbot/log/201711.log | grep "ラーメン" | egrep 'media' | sed -r 's/.*img="http:\/\/(.*)\/.*\/([A-Z])(.*g).*link.*/\/export\/space4\/yanai\/foodbot\/photo\/\1\/\2\/\2\3/'

nkf -u $source | grep $category | egrep 'media' | sed -r 's/.*img="http:\/\/(.*)\/.*\/([A-Z])(.*g).*link.*/\/export\/space4\/yanai\/foodbot\/photo\/\1\/\2\/\2\3/'# >> $output

echo "\n$source から $category の画像パスを抽出して $output ふぁいるへ書き込みました。"
echo "\nWrite Extracted ImagePATH of $category from $source to $output ."
