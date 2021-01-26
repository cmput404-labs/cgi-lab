#!/usr/bin/env python3

from templates import login_page, secret_page
import cgi
from secret import username, password
import os
import json
import cgitb
cgitb.enable()


##Q4: report POSDTed data

form = cgi.FieldStorage()

cookie = []
if 'HTTP_COOKIE' in os.environ:
    cookie = os.environ['HTTP_COOKIE'].split('; ')

if len(cookie) == 2:
    if(cookie[0] == 'Username=yo' and cookie[1] == 'Password=ho'):
        print(secret_page(username, password))

else:
    input_username = form.getfirst("username", "")
    input_password = form.getfirst("password", "")

    ##Q5: set cookie
    if (input_username == username and input_password == password):
        print (f"Set-Cookie:Username = {username};")
        print (f"Set-Cookie:Password = {password};")

    print('Content-Type: text/html')
    print()
    print("""
    <!doctype html>
    <html>
    <body>
    """)

    print(f"<p> username = {input_username}</p>")
    print(f"<p> password = {input_password}</p>")


    print("""
    </body>
    </html>
    """)
