import requests

# STEP 1: Ask the user for a city name

city = input("Enter a city name: ").strip()  #Strip use for removing any leading or trailing whitespace from the input.


if not city:
    print("City name cannot be empty. Please enter a valid city name.")
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

  
