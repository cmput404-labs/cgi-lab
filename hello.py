#!/usr/bin/env python3


import os
import json
from templates import login_page, _wrapper



##Q2: environmet back as json

# print('Content-Type: application/json')
# print()
# print(json.dumps(dict(os.environ), indent = 2))


##Q2: report value of query parameters

# print('Content-Type: text/html')
# print()
# print("""
# <!doctype html>
# <html>
# <body>
# <h1>Query</h1>
# """)

# print("<ul>")
# for para in os.environ['QUERY_STRING'].split('&'):
#     (name, value) = para.split('=')
#     print(f"<li><em>{name}</em> = {value}</li>")

# print("</ul>")

# print("""
# </body>
# </html>
# """)


##Q3: report users browser

# print('Content-Type: text/html')
# print()
# print("""
# <!doctype html>
# <html>
# <body>
# <h1>User browser</h1>
# """)

# print(f"<p> HTTP_USER_AGENT={os.environ['HTTP_USER_AGENT']}</p>")

# print("""
# </body>
# </html>
# """)

##Q4: login page
print(login_page())





