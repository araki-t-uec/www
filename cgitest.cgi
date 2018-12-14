#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi

html_body = """
<!DOCTYPE html>
<html>
<head>
<title>受信したデータを表示</title>
</head>
<body>
<h1>%s</h1>
<form action="./cgitest.cgi" method="POST">
  <input type="text" name="text" value="hoge" />  
  <input type="submit" name="submit" />
</form>

</body>
</html>
"""

form = cgi.FieldStorage()
text = form.getvalue('text','')



print("Content-type: text/html; charset=UTF-8\n\n")
print(html_body % (text))
