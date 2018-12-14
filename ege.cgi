#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgi
import cgitb
cgitb.enable()

import sys
sys.path.append('/home/yanai-lab/ege-t/www/simplejson/simplejson-2.5.2/')
import simplejson as json
import random
import codecs
import os
import glob

dir2id = {'images':1,
          'videos':2}


form = cgi.FieldStorage()
text = form.getvalue('text','')
checked_box = form.getvalue('chbx','')
radiobutton = form.getvalue('radioo','')

def body_content():
    
    dir_id = 0
    dir_name = ''
    f = cgi.FieldStorage()
    if f.has_key('id'):
        dir_id = int(f['id'].value)
    if f.has_key('dir'):
        dir_name = str(f['dir'].value)
    
    if dir_id==1: # _images
        img_list = sorted(glob.glob(dir_name+'/*'))
        body_html = ''
        for i, d in enumerate(img_list):
            body_html += '<p><a href="%s"><img src="%s" width="512">%s</a></p>\n' % (d,d,d)  
        return body_html

    elif dir_id==2: # _videos
        vid_list = sorted(glob.glob(dir_name+'/*.mp4'))
        body_html = ''
        for i, d in enumerate(vid_list):
            body_html += '<p><video src="%s" controls>%s</video></p>\n' % (d,d)  
        return body_html

    elif dir_id==3:
        pass
    elif dir_id==4:
        pass
    elif dir_id==5:
        pass
    elif dir_id==6:
        pass

    else:
        dir_list = [d for d in os.listdir('./') if os.path.isdir(d)]
        body_html = ''
        for i, d in enumerate(dir_list):
            if '_images' in d:
                body_html += '<p><a href="./?id=%d&dir=%s">%d %s</a></p>\n' % (1,d,i,d)
            elif '_videos' in d:
                body_html += '<p><a href="./?id=%d&dir=%s">%d %s</a></p>\n' % (2,d,i,d)
            else:
                body_html += '<p><a href="./%s">%d %s</a></p>\n' % (d,i,d)
        return body_html
    
'''/_/_/_/ html code /_/_/_/'''
def html_code():
    
    ####################################### title
    #######################################
    print '''Content-type: text/html\n'''
    print '''<html>'''
    print '''<head><meta charset="utf8">'''
    print '''<title>Results</title>'''
    print '''<link rel="stylesheet" type="text/css" href="css/main.css">'''
    print '''</head>'''
    
    ####################################### body
    #######################################
    print '''<body>'''
    print '''<h2>Results</h2>'''
    print body_content()
    hoge = '<input type=\"text\" name=\"text\" value="EGE">'
    print('''<form action="./ege.cgi" method="POST">''')
    print(hoge )
    print('''<p>
    <input type="checkbox" name="chbx" value="1" checked="checked"> 1
    <input type="checkbox" name="chbx" value="foo"> f
    <input type="checkbox" name="chbx" value="bar"> b
    </p>''')
    print('''<p>
    <input type="radio" name="radioo" value="reji" >matudaira
    <input type="radio" name="radioo" value="yuki" checked>izumi
    <input type="radio" name="radioo" value="takumi" >ide
    </p>''')
    print('''<input type="submit" name="submit"> </form>''')
    print'''<h1>'''
    print(text)
    print'''</h1>'''
    print('''<p>''')
    print(radiobutton)
    print('''</p>''')
    print('''<p>''')
    print(checked_box)
    print('''</p>''')
    print '''</body>'''
    print '''</html>'''
    
if __name__=='__main__':

    html_code()
