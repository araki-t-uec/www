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
passlist = Hash.new("nil") #ディレクトリとファイルを多次元配列で格納する
dirlist = '<option value="./Video/">./Video</option>\n' 
@list = ""      #HTMLファイルnameを格納する変数
text = ""       #実際にHTMLに出力される中身を格納する変数

myname = File.basename(__FILE__)

c = CGI.new(:accept_charset => "UTF-8")

def defdir(pass)
  #passに入っているディレクトリ以下の.htmlファイルを@list配列へ代入
  @list += `ls #{pass}*.mp4`
  #public_html以下の深度1までのディレクトリ(public_html/*/)まで再帰
#  if /\*\/\*\// =~ pass #深度2まで
  if /\*\// =~ pass
  else
    defdir(pass += "*/")
  end
end

defdir(dir)

#@listからディレクトリとファイルを取り出し、キーとバリューでpasslistへ代入
@list.each_line do |line|
  if /(\S+\/)(\S+:)/ =~ line
   #ディレクトリの時は無視
  elsif /(\S+\/)(\S+.mp4)\Z/ =~ line || /(\S+\/)(\S+.gif)\Z/ =~ line
#   elsif /(\S+\/)(\S+.*)/ =~ line
    if passlist[$1] == "nil"
      passlist[$1] = Array.new
    end
    passlist[$1] << $2
    #  "../" => ["a.html", "b.html", "c.html"]
  end
end


#passlistからファイルを取り出し、htmlタグをつけてtext変数へ代入。
text += ""
passlist.keys.each do |pass|
  n=0
  dirlist += "<option value=\"#{pass}\">#{pass}</option>\n"
  text += "<h2> #{pass} </h2>\n <table>\n<tr>"
  passlist[pass].each do |file|
    n+=1
    text += "<td><video controls src=\"#{pass}#{file}\" preload=\"metadata\"></video><br>#{file}</td>\n"
    if n%5 == 0
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

