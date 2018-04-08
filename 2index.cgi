#!/usr/bin/env ruby
# coding: utf-8

#このプログラムは、自身のpublic_htmlの中の全ての.htmlファイルを一覧表示するWebページを作成する


require 'cgi'
css = "../main.css"
current="./"   #このプログラムの置いてあるディレクトリからpublic_htmlへ移動するためのパス
pwd = `pwd | sed "s/ //g"` + "/"
passlist = Hash.new("nil") #ディレクトリとファイルを多次元配列で格納する
@list = ""      #HTMLファイルnameを格納する変数
text = ""       #実際にHTMLに出力される中身を格納する変数



c = CGI.new(:accept_charset => "UTF-8")

def defdir(pass)
  #passに入っているディレクトリ以下の.htmlファイルを@list配列へ代入
#  @list += `ls #{pass}*.html`
   @list += `ls #{pass}*`
  #public_html以下の深度2までのディレクトリ(public_html/*/*/)まで再帰
  if /\*\/\*\// =~ pass
  else
    defdir(pass += "*/")
  end
end

#public_htmlまでのパスを引数に、defdirメソッドを呼び出す
defdir(current)


#@listからディレクトリとファイルを取り出し、キーとバリューでpasslistへ代入
@list.each_line do |line|
   if /(\S+\/)(\S+:)/ =~ line
   #ディレクトリの時は無視
#  if /(\S+\/)(\S+.html)/ =~ line
   elsif /(\S+\/)(\S+.*)/ =~ line
    if passlist[$1] == "nil"
      passlist[$1] = Array.new
    end
    passlist[$1] << $2
    #  "../" => ["a.html", "b.html", "c.html"]
  end
end


#passlistからファイルを取り出し、htmlタグをつけてtext変数へ代入。
text += "<dl>\n"
passlist.keys.each do |pass|
  text += "<dt>#{pass}\n"
  passlist[pass].each do |file|
    text += "<dd><a href=\"#{pass}#{file}\">#{file}</a></dd>\n"
  end
  text += "</dt>\n"
end
text += "</dl>\n"


# 以下、HTML出力

print "Content-type: text/html; charset=UTF-8\n\n"
printf(<<_EOS_, css, text)

<!DOCTIPE html>
<head>
<title>Link List</title>
<link rel="stylesheet" type="type/css" href="%s">
</head>
<body>
<h1>Link List</h1>
<p>cullent dir is "#{pwd}"</p>
<p>%s</p>

</body>
</html>

_EOS_
