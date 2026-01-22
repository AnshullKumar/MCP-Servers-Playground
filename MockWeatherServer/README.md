# Mock Weather MCP Server

This project is a mock server that provides weather information, the current time, and a simple calculator service. It is built using FastMCP.

## Features

The server exposes the following tools:

*   **`get_weather(city: str)`**: Retrieves the real-time weather for a given city using the Open-Meteo API. No API key is required.
*   **`get_time(timezone: str)`**: Returns the current time in the specified timezone (supports "UTC" and "IST").
*   **`calculate(expression: str)`**: Evaluates a simple mathematical expression.

## How it Works

This project consists of two main Python files: a server (`my_server.py`) and a client (`test_client.py`).

### The Server (`my_server.py`)

*   The server is built using the **`FastMCP`** library, which simplifies the process of creating a server with callable "tools".
*   It defines three functions (`get_weather`, `get_time`, and `calculate`) and marks them as tools using the `@mcp.tool` decorator. This decorator makes the functions available to be called by any connected client.
*   **`get_weather(city)`**: This tool takes a city name, calls the free Open-Meteo geocoding API to find the city's latitude and longitude, and then calls the Open-Meteo weather API to get the current weather data. It then returns the weather information to the client.
*   **`get_time(timezone)`**: This tool calculates and returns the current time, with support for UTC and IST timezones.
*   **`calculate(expression)`**: This tool takes a string containing a simple math expression, evaluates it, and returns the result.
*   When you run `python my_server.py`, the server starts and waits for a client to connect.

### The Client (`test_client.py`)

*   The client is an interactive command-line application that allows you to use the tools defined on the server.
*   It uses the **`fastmcp.Client`** to connect to the server.
*   It displays a menu of the available operations (Get Weather, Get Time, Calculate).
*   When you select an option, the client prompts you for the necessary input (like a city name or a math expression).
*   It then uses the `client.call_tool()` method to send a request to the server to execute the corresponding tool with the input you provided.
*   Finally, it receives the result from the server and prints it in a user-friendly format.

### Client-Server Interaction

1.  The server (`my_server.py`) starts first and listens for connections.
2.  The client (`test_client.py`) connects to the server.
3.  The user chooses an operation in the client.
4.  The client sends the tool name and its parameters to the server.
5.  The server executes the requested tool function.
6.  The server sends the result back to the client.
7.  The client displays the result to the user.

This separation of concerns allows the "heavy lifting" (like calling external APIs or performing complex calculations) to be done on the server, while the client simply provides a way for the user to interact with the server's capabilities.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/AnshullKumar/mock-weather-mcp-server.git
    cd mock-weather-mcp-server
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Server and Client

1.  **Start the server:**
    Open a terminal and run:
    ```bash
    python my_server.py
    ```

2.  **Run the client:**
    Open a *second* terminal and run:
    ```bash
    python test_client.py
    ```
    Now you can interact with the server through the client's menu.

