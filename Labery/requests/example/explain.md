# How `requests` Works

Let's imagine a weather application.

You type:

```text
Kolkata
```

Your application needs weather information.

The architecture might look like:

```text
                Internet
                   ↓
Your Python App → Weather API
                   ↓
             Weather Data
                   ↓
              Python App
                   ↓
          "Temperature: 31°C"
```

`requests` can help Python communicate with the API.

For example:

```python
import requests

response = requests.get("https://example.com")

print(response.status_code)
```

You don't need to understand every part yet.

Focus on this:

```python
requests.get(...)
```

means:

> "Send a GET request."

---

## What Is a Response?

When your Python program asks a server something, the server sends something back.

For example:

```text
Python
  ↓
"Give me weather information"
  ↓
Server
  ↓
"Temperature = 31°C"
  ↓
Python
```

The returned thing is called a **response**.

So:

```python
response = requests.get(...)
```

means:

```text
requests.get()
      ↓
Server response
      ↓
response variable
```

---

## Status Code

Servers often return a status code.

For example:

```python
print(response.status_code)
```

Common meanings:

| Code | Meaning |
| :--: | :------ |
|  200 | Success |
|  404 | Not Found |
|  500 | Server Error |

So you might do:

```python
import requests

response = requests.get("https://example.com")

print(response.status_code)
```

If you get:

```text
200
```

it generally means the request succeeded.

---

## What Are Status Codes?

| Code | Meaning | Hinglish |
| :--: | :------ | :------- |
| 200 | OK | Request successful |
| 201 | Created | Naya data create hua |
| 400 | Bad Request | Request galat hai |
| 401 | Unauthorized | Permission nahi hai |
| 403 | Forbidden | Access allowed nahi hai |
| 404 | Not Found | Data nahi mila |
| 500 | Server Error | Server mein problem hai |
