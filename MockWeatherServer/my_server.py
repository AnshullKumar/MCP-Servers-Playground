import csv
import os
from datetime import datetime, timedelta
from fastmcp import FastMCP

# Initialize the server with a name
mcp = FastMCP("my-first-server")

# --- Load Weather Data ---
def load_weather_data():
    """Loads weather data from the CSV file into a dictionary."""
    data = {}
    file_path = os.path.join(os.path.dirname(__file__), "weather_data.csv")
    try:
        with open(file_path, mode='r', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                city_name = row["city"].lower()
                data[city_name] = {
                    "temp": int(row["temperature"]),
                    "condition": row["condition"],
                }
    except FileNotFoundError:
        print(f"Warning: Weather data file not found at {file_path}")
    return data

weather_data = load_weather_data()
# -------------------------

@mcp.tool
def get_weather(city: str) -> dict:
    """Get the current weather for a city from the dataset."""
    city_lower = city.lower()
    if city_lower in weather_data:
        return {"city": city, **weather_data[city_lower]}
    else:
        # Return a default response if the city is not found
        return {"city": city, "error": "Weather data not found for this city."}

@mcp.tool
def get_time(timezone: str = "UTC") -> str:
    """Get the current time in a specified timezone. Supports UTC and IST."""
    now = datetime.utcnow()
    if timezone.upper() == "IST":
        # Note: This is a simplified IST calculation (UTC+5:30)
        now += timedelta(hours=5, minutes=30)
        return f"Current time (IST): {now.strftime('%H:%M:%S')}"
    
    # Default to UTC
    return f"Current time (UTC): {now.strftime('%H:%M:%S')}"


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