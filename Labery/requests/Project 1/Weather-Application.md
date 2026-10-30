# What is a Response? Let's Build a Real Weather Application 🌦️

Today we're going to understand one of the most important concepts in Python:

> **Request → Server → Response**

And then we'll build a working Weather Application using Python and the `requests` library.

I'll explain everything in simple English + Hinglish, assuming you're a beginner.

---

## 1. First, what is a Response?

Imagine you go to a restaurant.

1. You ask the waiter for a pizza.
2. The waiter sends your order to the kitchen.
3. The kitchen prepares the pizza.
4. The waiter brings the pizza back to you.

This is similar to how the internet works.

![](https://images.openai.com/static-rsc-4/zIifRG8AU2NcDRs3U7WX2Ci-ChdGsLZTR7i3i6f3V2Ptfj9E7JvBJOHDTdx2T69wfANbVRLtrQmwN_4oXdxbVyRZZjdob2TQcnaOdBG811lBVLwwj-m7CyPFg_QaToCRF0FPIqJj8NeJwyGslBP9uzj3U6rqcFCMidS7X2hKfl2zxC0v15_Ougn9lsj56yCS?purpose=fullsize)

In programming:

| Restaurant | Python / Internet |
| :--- | :--- |
| You | Python program |
| Ask for pizza | Request |
| Kitchen | Server |
| Prepared pizza | Response data |
| Pizza delivered | Response received |

> **English:** A response is the information that a server sends back after receiving a request from your program.

> **Hinglish:** Jab Python kisi server se kuch information maangta hai, toh server jo information wapas bhejta hai, usko Response kehte hain.

For example:

```text
Python Program
      |
      | Request: Give me Kolkata weather
      ↓
Weather Server
      |
      | Response: 31°C, Humidity 70%
      ↓
Python Program
```

*That's a response!*

---

## 2. What is an API?

API stands for Application Programming Interface.

Think of an API as a bridge between two applications.

For example:

- Your Python application wants weather information.
- A weather service has weather information.
- The API allows your application to request that information.

![](https://images.openai.com/static-rsc-4/I9iIBgg3myFTPbfrAxsB9kLc4rviibnvurOpj0GVAGpmNXRw0LRl_0d5YMp1WcaXyeD2cMd1mIbNETmARPNnm8lKiqY9YTikAHCKrL6V8VjeegZ-a1iIHM12VANZzxlzTN1rNBfWqqzRPNZQOPy1wDpQb6l7cKKq5uWDI1lHj6YToVEbVmEm_qvDtQ58RudD?purpose=fullsize)

> **Hinglish:** API ek messenger ya bridge ki tarah kaam karta hai. Aapki application API ke through doosre server se data maang sakti hai.

---

## 3. Understand the response using Python

First, install the library.

Open your terminal:

```bash
python -m pip install requests
```

Now create a Python file:

`response_demo.py`

Write:

```python
import requests

response = requests.get("https://example.com")

print(response)
print(response.status_code)
print(response.text)
```

Let's understand each line.

**Line 1:**

```python
import requests
```

We are importing the requests library.

**Line 2:**

```python
response = requests.get("https://example.com")
```

We are sending a GET request to a website.

**Line 3:**

```python
print(response)
```

Displays information about the response.

**Line 4:**

```python
print(response.status_code)
```

Displays the HTTP status code.

**Line 5:**

```python
print(response.text)
```

Displays the response body as text.

### What are status codes?

| Code | Meaning | Hinglish |
| :---: | :--- | :--- |
| 200 | OK | Request successful |
| 201 | Created | Naya data create hua |
| 400 | Bad Request | Request galat hai |
| 401 | Unauthorized | Permission nahi hai |
| 403 | Forbidden | Access allowed nahi hai |
| 404 | Not Found | Data nahi mila |
| 500 | Server Error | Server mein problem hai |

Remember: A response is more than just a status code. It can also contain data, headers and other information.

---

## 4. What does a real weather response look like?

Imagine you request Kolkata's weather.

The weather server might return data like this:

```json
{
    "city": "Kolkata",
    "temperature": 31,
    "humidity": 70,
    "wind_speed": 12
}
```

This is JSON data.

Your Python program can read this data and display:

```text
City: Kolkata
Temperature: 31°C
Humidity: 70%
Wind Speed: 12 km/h
```

Now let's build the actual application.

---

## 5. Build our real Weather Application

*Beginner-friendly project* | *Real API*

We're going to use Open-Meteo, a weather service that provides weather data through an API.

Good news:

- No API key required for basic use.
- No account registration required.
- Works with real city names.
- Provides temperature, humidity, wind speed and weather conditions.

See its official documentation: Open-Meteo API documentation.

<https://open-meteo.com/en/docs>

Open Meteo+1

Our application will work like this:

```text
Your Python Weather App

You enter a city name

Step 1 — Geocoding API

Find the city's latitude and longitude

Step 2 — Weather API

Get temperature, humidity and wind

Display weather information

Show the result to the user
```

### Why do we need two APIs?

Because the weather API needs coordinates, not just a city name.

For example:

```text
Kolkata
   ↓
Geocoding API
   ↓
Latitude: 22.57
Longitude: 88.36
   ↓
Weather API
   ↓
Temperature: 31°C
```

These coordinates are illustrative; the API will return the actual coordinates.

---

## 6. Step-by-step installation

### Step 1. Create a project folder

Create a folder called:

`weather_project`

### Step 2. Open the folder in VS Code

Create a file:

`weather.py`

Your folder should look like:

```text
weather_project/
    weather.py
```

### Step 3. Open the VS Code terminal

Install requests:

```bash
python -m pip install requests
```

### Step 4. Check installation

Run:

```bash
python -m pip show requests
```

If you see package information, installation was successful.

---

## 7. Complete working Weather App code

Copy this entire code into `weather.py`.

```python
import requests

# STEP 1: Ask the user for a city
city = input("Enter city name: ").strip()

if not city:
    print("Please enter a city name.")

else:
    try:
        # STEP 2: Find city coordinates
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"

        geo_params = {
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        }

        geo_response = requests.get(
            geo_url,
            params=geo_params,
            timeout=10
        )

        # Check whether request succeeded
        geo_response.raise_for_status()

        # Convert JSON response into Python dictionary
        geo_data = geo_response.json()

        # Check whether city was found
        if not geo_data.get("results"):
            print("City not found. Please try another city.")

        else:
            # STEP 3: Extract city information
            location = geo_data["results"][0]

            city_name = location["name"]
            country = location.get("country", "Unknown")

            latitude = location["latitude"]
            longitude = location["longitude"]

            # STEP 4: Request weather information
            weather_url = "https://api.open-meteo.com/v1/forecast"

            weather_params = {
                "latitude": latitude,
                "longitude": longitude,
                "current": (
                    "temperature_2m,"
                    "relative_humidity_2m,"
                    "apparent_temperature,"
                    "wind_speed_10m,"
                    "weather_code"
                ),
                "timezone": "auto"
            }

            weather_response = requests.get(
                weather_url,
                params=weather_params,
                timeout=10
            )

            weather_response.raise_for_status()

            # STEP 5: Convert response into Python dictionary
            weather_data = weather_response.json()

            # STEP 6: Extract current weather
            current = weather_data["current"]

            temperature = current["temperature_2m"]
            humidity = current["relative_humidity_2m"]
            feels_like = current["apparent_temperature"]
            wind_speed = current["wind_speed_10m"]
            weather_code = current["weather_code"]

            # STEP 7: Describe weather condition
            weather_conditions = {
                0: "Clear sky",
                1: "Mainly clear",
                2: "Partly cloudy",
                3: "Overcast",
                45: "Fog",
                48: "Depositing rime fog",
                51: "Light drizzle",
                53: "Moderate drizzle",
                55: "Dense drizzle",
                61: "Slight rain",
                63: "Moderate rain",
                65: "Heavy rain",
                71: "Slight snowfall",
                73: "Moderate snowfall",
                75: "Heavy snowfall",
                80: "Slight rain showers",
                81: "Moderate rain showers",
                82: "Violent rain showers",
                95: "Thunderstorm"
            }

            condition = weather_conditions.get(
                weather_code,
                "Other weather condition"
            )

            # STEP 8: Display weather report
            print("\n" + "=" * 35)
            print("       WEATHER REPORT")
            print("=" * 35)

            print(f"City: {city_name}")
            print(f"Country: {country}")
            print(f"Temperature: {temperature} °C")
            print(f"Feels Like: {feels_like} °C")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} km/h")
            print(f"Condition: {condition}")

            print("=" * 35)

    except requests.exceptions.Timeout:
        print("Request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        print("Internet connection problem.")

    except requests.exceptions.HTTPError as error:
        print("Server returned an HTTP error:", error)

    except requests.exceptions.RequestException as error:
        print("Request failed:", error)

    except (KeyError, IndexError, TypeError, ValueError):
        print("Unexpected data received from the weather server.")
```

---

## 8. How to run this project

Open your terminal inside `weather_project`.

Run:

```bash
python weather.py
```

It will ask:

```text
Enter city name:
```

Type:

`Kolkata`

Your output will look something like:

```text
===================================
       WEATHER REPORT
===================================
City: Kolkata
Country: India
Temperature: 31.2 °C
Feels Like: 35.0 °C
Humidity: 70%
Wind Speed: 12.5 km/h
Condition: Partly cloudy
===================================
```

---

## 9. Now understand the code like a developer

Don't just copy the code. Let's understand what is happening.

### A. Taking input from the user

```python
city = input("Enter city name: ").strip()
```

> **English:** Asks the user to enter a city.

> **Hinglish:** User se city ka naam le rahe hain. `.strip()` extra spaces remove karta hai.

Example:

`"  Kolkata  " → "Kolkata"`

### B. Sending a request

```python
geo_response = requests.get(
    geo_url,
    params=geo_params,
    timeout=10
)
```

This is one of the most important lines.

Let's break it down:

| Code | Meaning |
| :--- | :--- |
| `requests` | Our library |
| `.get()` | Send a GET request |
| `geo_url` | Where to send the request |
| `params` | Information we're sending |
| `timeout=10` | Don't wait forever |

> **Hinglish:** Hum server ko bol rahe hain: "Mujhe is city ki location information do."

### C. What is response.json()?

This is probably the most important concept in today's lesson.

```python
geo_data = geo_response.json()
```

The server returns JSON data.

For example, imagine the server returns:

```json
{
    "results": [
        {
            "name": "Kolkata",
            "country": "India",
            "latitude": 22.57,
            "longitude": 88.36
        }
    ]
}
```

Python reads that JSON and converts it into a Python dictionary.

**Before:**

```text
JSON response from server
```

**After:**

```python
geo_data = {
    "results": [
        {
            "name": "Kolkata",
            "country": "India",
            "latitude": 22.57,
            "longitude": 88.36
        }
    ]
}
```

Now you can access the information:

```python
print(geo_data["results"][0]["name"])
```

**Output:**

```text
Kolkata
```

> **Hinglish:** `.json()` server se aaye JSON data ko Python dictionary/list mein convert karta hai, jisse hum easily data access kar sakte hain.

### D. Extracting the information

```python
current = weather_data["current"]
```

This accesses the current weather section.

Then:

```python
temperature = current["temperature_2m"]
humidity = current["relative_humidity_2m"]
```

We're extracting individual values.

Imagine this is your dictionary:

```python
current = {
    "temperature_2m": 31,
    "relative_humidity_2m": 70
}
```

You can access:

```python
print(current["temperature_2m"])
```

**Output:**

```text
31
```

### E. Displaying the information

```python
print(f"Temperature: {temperature} °C")
```

The f before the string is called an f-string.

It allows you to put variables inside text.

Example:

```python
name = "Rahul"
age = 22

print(f"My name is {name} and I am {age} years old.")
```

**Output:**

```text
My name is Rahul and I am 22 years old.
```

### F. Handling errors

What happens if the internet stops working?

What happens if the user enters a city that doesn't exist?

What happens if the server doesn't respond?

That's why we use:

```python
try:
    # Main code

except:
    # Error handling
```

Our actual code uses more specific exception types, which is better practice.

For example:

```python
except requests.exceptions.ConnectionError:
    print("Internet connection problem.")
```

> **Hinglish:** Agar internet band ho jaye ya server se connection na ho, toh program crash hone ke bajaye user ko understandable message dikha sakta hai.

---

## 10. Understand the most important response properties

Whenever you use requests, remember these:

| Property / Method | What it does |
| :--- | :--- |
| `response.status_code` | Shows HTTP status |
| `response.text` | Returns response body as text |
| `response.json()` | Converts JSON response to Python data |
| `response.headers` | Shows response headers |
| `response.url` | Shows the final request URL |
| `response.raise_for_status()` | Raises an error for HTTP error responses |

One important difference:

`response.text`

and

`response.json()`

are not the same.

- `.text` gives you text.
- `.json()` gives you Python data converted from JSON.

You can learn more from the official Requests documentation.

---

## 11. Practice challenges

Now I want you to modify the weather application yourself.

### Your coding homework

0/5 completed

- [ ] Change the application so that it asks for your favourite city.
  - Hint: Use `input()` and store it in a variable.

- [ ] Display only temperature and humidity.
  - Hint: Use `current['temperature_2m']` and `current['relative_humidity_2m']`.

- [ ] Add the feels-like temperature.
  - Hint: Find `apparent_temperature` in the API response.

- [ ] Try entering Mumbai, Delhi and London.
  - Hint: Run the program three times with different cities.

- [ ] What happens when you enter an invalid city?
  - Hint: Check the results list before extracting location details.

---

## 12. What have you learned today?

### Your progress

- [ ] What is a request?
- [ ] What is a response?
- [ ] What is an API?
- [ ] How to install requests
- [ ] How to use requests.get()
- [ ] How to read response.json()
- [ ] How to build a real API project
