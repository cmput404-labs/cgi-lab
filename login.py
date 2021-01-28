#!/usr/bin/env python3

from templates import login_page, secret_page, after_login_incorrect
import cgi
from secret import username, password
import os
import json
import cgitb
cgitb.enable()

from http.cookies import SimpleCookie

##Q4: report POSDTed data

form = cgi.FieldStorage()

c = SimpleCookie(os.environ['HTTP_COOKIE'])
c_username = None
c_password = None

if c.get("Username"):
    c_username = c.get("Username").value

if c.get("Password"):
    c_password = c.get("Password").value



if(c_username==username and c_password==password):
    print(secret_page(username, password))

else:    
    input_username = form.getfirst("username", "")
    input_password = form.getfirst("password", "")

    if input_username=="" and input_password=="":
        print(login_page())
    else:
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

            print(f"<p> login correct</p>")

            print("""
            </body>
            </html>
            """)

        else:
            print(after_login_incorrect())

    ## print username and password
    # print('Content-Type: text/html')
    # print()
    # print("""
    # <!doctype html>
    # <html>
    # <body>
    # """)

    # print(f"<p> username = {input_username}</p>")
    # print(f"<p> password = {input_password}</p>")


    # print("""
    # </body>
    # </html>
    # """)
