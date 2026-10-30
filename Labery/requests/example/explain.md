Let's imagine a weather application.

You type:

Kolkata

Your application needs weather information.

The architecture might look like:

                Internet
                   ↓
Your Python App → Weather API
                   ↓
             Weather Data
                   ↓
              Python App
                   ↓
          "Temperature: 31°C"


requests can help Python communicate with the API.

For example:

import requests

response = requests.get("https://example.com")

print(response.status_code)


You don't need to understand every part yet.

Focus on this:

requests.get(...)

means:
"Send a GET request."

What is a response?

When your Python program asks a server something, the server sends something back.

For example:

Python
  ↓
"Give me weather information"
  ↓
Server
  ↓
"Temperature = 31°C"
  ↓
Python

The returned thing is called a response.

So:

response = requests.get(...)


means:

requests.get()
      ↓
Server response
      ↓
response variable

Status code

Servers often return a status code.

For example:

print(response.status_code)

Common meanings:

200 → Success
404 → Not Found
500 → Server Error

So you might do:

import requests

response = requests.get("https://example.com")

print(response.status_code)

If you get:

200

it generally means the request succeeded.




What are status codes?

Code	Meaning	         Hinglish
200 	OK	             Request successful
201	    Created	         Naya data create hua
400	    Bad              Request	Request galat hai
401	    Unauthorized	 Permission nahi hai
403	    Forbidden	     Access allowed nahi hai
404	    Not Found	    Data nahi mila
500	    Server Error	Server mein problem hai