#!/usr/bin/env ruby
# -*- coding:utf-8 -*-

require 'cgi'
receive = CGI.new
dir = receive["dir"]
if dir == ""
	dir="./Video/"
end
css = "./css/img.css"
#pwd = `pwd | sed "s/ //g"` + "/"
pathlist = Hash.new("nil") #ディレクトリとファイルを多次元配列で格納する
dirlist = '<option value="./Video/">./Video</option>\n' 
@list = ""      #HTMLファイルnameを格納する変数
text = ""       #実際にHTMLに出力される中身を格納する変数
cols = 5

myname = File.basename(__FILE__)

c = CGI.new(:accept_charset => "UTF-8")

def defdir(path)
  #pathに入っているディレクトリ以下の.htmlファイルを@list配列へ代入
  @list += `ls #{path}| grep "/"`
  @list += `ls #{path}*.mp4`
  @list += `ls #{path}*.avi`
  #public_html以下の深度1までのディレクトリ(public_html/*/)まで再帰
#  if /\*\/\*\// =~ path #深度2まで
  if /\*\// =~ path
  else
    defdir(path += "*/")
  end
end

defdir(dir)

#@listからディレクトリとファイルを取り出し、キーとバリューでpathlistへ代入
@list.each_line do |line|
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
    text += "<td><video controls src=\"#{path}#{file}\" preload=\"metadata\"></video><br>#{file}</td>\n"
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
<title>VIDEOs</title>
<link rel="stylesheet" type="text/css" href="%s">
</head>
<body>
<form method="POST" action="#{myname}">
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

