import requests

import json

BASE_URL='http://127.0.0.1:7878/'
ENDPOINT='api/'

r=requests.get(BASE_URL+ENDPOINT+'users/')

data=r.json()

emp=data[0]
print("Employee Name:",emp['username'])
print("Employee id:",emp['email'])
print("Employee status:",emp['is_staff'])