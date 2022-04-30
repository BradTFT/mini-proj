#! idea for a password lock wall
#! works
from dotenv import load_dotenv
from os import getenv
load_dotenv()
password = getenv("password")

input = input('Password >>> ')
if input == password:
    grantaccess = print(getenv('content'))
    grantaccess
else:
    denyaccess = print('Access Denied')
    denyaccess
