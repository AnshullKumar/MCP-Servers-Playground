import requests
from datetime import datetime, timedelta
import pytz # Import pytz
from fastmcp import FastMCP

# Initialize the server with a name
mcp = FastMCP("my-first-server")

@mcp.tool
def get_weather(city: str) -> dict:
    """Get the current weather for a city using the Open-Meteo API."""
    try:
        # Step 1: Get latitude and longitude for the city from Open-Meteo's geocoding API
        geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
        geo_response = requests.get(geocoding_url)
        geo_response.raise_for_status()
        geo_data = geo_response.json()

        if not geo_data.get("results"):
            return {"error": f"Could not find location data for '{city}'."}

        location = geo_data["results"][0]
        latitude = location["latitude"]
        longitude = location["longitude"]
        
        # Step 2: Get the current weather using the latitude and longitude
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
        weather_response = requests.get(weather_url)
        weather_response.raise_for_status()
        weather_data = weather_response.json()

        if "current_weather" in weather_data:
            current_weather = weather_data["current_weather"]
            return {
                "city": location.get("name", city),
                "temperature": f"{current_weather['temperature']}°C",
                "wind_speed": f"{current_weather['windspeed']} km/h",
            }
        else:
            return {"error": "Could not retrieve current weather data."}

    except requests.exceptions.RequestException as e:
        return {"error": f"API request failed: {e}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}

@mcp.tool
def get_time(timezone: str = "UTC") -> str:
    """
    Get the current time in a specified timezone. Uses pytz for accurate conversion.
    Returns a formatted time string or an error string if the timezone is invalid.
    """
    try:
        # Get current UTC time
        utc_now = datetime.utcnow().replace(tzinfo=pytz.utc)
        
        # Convert to specified timezone
        tz = pytz.timezone(timezone)
        localized_time = utc_now.astimezone(tz)
        
        return f"Current time ({timezone}): {localized_time.strftime('%H:%M:%S %Z%z')}"
    except pytz.exceptions.UnknownTimeZoneError:
        return f"Error: Unknown timezone '{timezone}'. Please use a valid IANA timezone (e.g., 'America/New_York', 'Asia/Kolkata')."
    except Exception as e:
        return f"Error: An unexpected error occurred: {e}"


@mcp.tool
def calculate(expression: str) -> dict:
    """Safely evaluate a mathematical expression."""
    try:
        # Only allow safe math operations
        allowed_chars = set("0123456789+-*/.() ")
        if not all(c in allowed_chars for c in expression):
            return {"error": "Invalid characters in expression"}
        
        result = eval(expression)  # Safe because we validated input
        return {"expression": expression, "result": result}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    mcp.run(transport="stdio")