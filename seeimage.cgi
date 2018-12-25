#!/usr/bin/env ruby
# -*- coding:utf-8 -*-

require 'cgi'
receive = CGI.new
dir = receive["dir"]
if dir == ""
	dir="./Img/"
end

extensions = ["png","jpg","pdf","mp4"]

css = "./css/img.css"
#pwd = `pwd | sed "s/ //g"` + "/"
pathlist = Hash.new("nil") #ディレクトリとファイルを多次元配列で格納する
dirlist = '<option value="./Img/">./Img</option>\n' 
@list = ""      #HTMLファイルnameを格納する変数
text = ""       #実際にHTMLに出力される中身を格納する変数
cols = 6


c = CGI.new(:accept_charset => "UTF-8")

def defdir(path, extends)
  #pathに入っているディレクトリ以下の.htmlファイルを@list配列へ代入
  @list += `ls #{path}| grep "/"`
  for ext in extends
   @list +=`ls #{path}*.#{ext}`
  end
##  @list += `ls #{path}*.jpg #{path}*.pdf #{path}*.png`
#  @list += `ls #{path}*.jpg`
#  @list += `ls #{path}*.png`
#  @list += `ls #{path}*.pdf`
#  @list += `ls #{path}*.mp4`
  
  #public_html以下の深度1までのディレクトリ(public_html/*/)まで再帰
#  if /\*\/\*\// =~ path #深度2まで
  if /\*\// =~ path
  else
    defdir(path += "*/", extends)
  end
end

defdir(dir, extensions)

#print(@list)

#@listからディレクトリとファイルを取り出し、キーとバリューでpathlistへ代入
@list.each_line do |line|
#  if /(\S+\/)(\S+.[png|jpg|pdf|mp4])\Z/ =~ line
  if /(\S+\/)(\S+)\Z/ =~ line
    firstname = $1
    lastname = $2
    if pathlist[firstname] == "nil"
      pathlist[firstname] = Array.new
    end
    if /\S+\./ =~ lastname
      # 拡張子あり（ふぁいる）なら配列へ
      pathlist[firstname] << lastname
    end
    #  "../" => ["a.png", "b.png", "c.jpg"]
  end
end

#pathlistからファイルを取り出し、htmlタグをつけてtext変数へ代入。
text += ""
pathlist.keys.each do |path|
  n=0
  dirlist += "<option value=\"#{path}\">#{path}</option>\n"
  text += "<h2> #{path} </h2>\n <table>\n<tr>"
  pathlist[path].each do |file|
    n+=1
    text += "<td><a href=\"#{path}#{file}\"><img src=\"#{path}#{file}\"></a><br>#{file}</td>\n"
    if n%cols == 0
        text+="</tr><tr>"
    end
  end
  text += "</tr></table><br>\n"

end
text += "\n"


# HTML出力

print "Content-type: text/html; charset=UTF-8\n\n"
printf(<<_EOS_, css, text)

<!DOCTIPE html>
<head>
<title>output work</title>
<link rel="stylesheet" type="text/css" href="%s">
</head>
<body>
<form method="POST" action="seeimage.cgi">
<select name="dir">
#{dirlist}</select>
<input type="submit" value="go">
</form>
<h1>Images</h1>
<h2>dir is "#{dir}"</h2>
%s

</body>
</html>

_EOS_

