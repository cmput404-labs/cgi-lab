#!/usr/bin/env python3


import os
import json
from templates import login_page

#environmet back as json

print('Content-Type: application/json')
print()
print(json.dumps(dict(os.environ), indent = 2))


#report value of query parameters

print('Content-Type: text/html')
print()
print("""
<!doctype html>
<html>
<body>
""")

print(f"<p> QUERY_STRING={os.environ['QUERY_STRING']}</p>")
print("<ul>")
for para in os.environ['QUERY_STRING'].split('&'):
    (name, value) = para.split('=')
    print(f"<li><em>{name}</em> = {value}</li>")

print("</ul>")

print("""
</body>
</html>
""")


#report users browser