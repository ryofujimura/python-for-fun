import requests

r = requests.get("https://cuscousainc.com/")       
print("Line")
print(r.status_code)