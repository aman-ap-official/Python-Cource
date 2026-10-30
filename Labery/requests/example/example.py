import requests

response = requests.get("https://api.github.com")



print(response)
print(response.status_code)
print(response.text)

# Let's understand each line.

# Line 1:

# import requests

# We are importing the requests library.

# Line 2:

# response = requests.get("https://example.com")

# We are sending a GET request to a website.

# Line 3:

# print(response)

# Displays information about the response.

# Line 4:

# print(response.status_code)

# Displays the HTTP status code.

# Line 5:

# print(response.text)

# Displays the response body as text.

