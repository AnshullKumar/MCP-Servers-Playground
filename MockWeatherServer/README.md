# Mock Weather MCP Server

This project is a mock server that provides weather information, the current time, and a simple calculator service. It is built using FastMCP.

## Features

The server exposes the following tools:

*   **`get_weather(city: str)`**: Retrieves the weather for a given city. The weather data is sourced from `weather_data.csv`.
*   **`get_time(timezone: str)`**: Returns the current time in the specified timezone (supports "UTC" and "IST").
*   **`calculate(expression: str)`**: Evaluates a simple mathematical expression.

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

## Running the Server

To start the server, run the following command:

```bash
python my_server.py
```

The server will start and be ready to accept connections.

## Running the Client

To interact with the server, you can use the provided test client:

```bash
python test_client.py
```

The client will present you with a menu of options to choose from:

*   Get Weather
*   Get Time
*   Calculate
*   Quit

Follow the on-screen prompts to use the server's tools.

## Weather Data

The weather data is stored in `weather_data.csv`. You can add more cities and their weather conditions to this file to expand the dataset. Each row should contain a `city`, `temperature`, and `condition`.
