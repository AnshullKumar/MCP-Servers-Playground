import asyncio
from fastmcp import Client

# Helper function to print results clearly
def print_pretty_result(tool_name: str, result: dict):
    print(f"\n--- Result for {tool_name} ---")
    if "error" in result:
        print(f"  Error: {result['error']}")
    else:
        for key, value in result.items():
            print(f"  {key.replace('_', ' ').capitalize()}: {value}")
    print("---------------------------\n")

async def main():
    # Point the client at your server file
    client = Client("my_server.py")
    
    # Connect to the server
    async with client:
        print("Connected to the MCP server.")
        
        while True:
            print("\n" + "="*50)
            print("Which operation would you like to perform?")
            print("1. Get Weather")
            print("2. Get Time")
            print("3. Calculate")
            print("4. Quit")
            choice = input("Enter your choice (1-4): ")
            print("="*50 + "\n")

            if choice == '1':
                # --- Get Weather ---
                city_input = input("Enter a city for weather (e.g., Mumbai, London, Tokyo): ")
                print(f"Calling get_weather for {city_input}...")
                call_result = await client.call_tool(
                    "get_weather", 
                    {"city": city_input}
                )
                if call_result.is_error:
                    print_pretty_result("Get Weather", {"error": call_result.data["error"]})
                else:
                    print_pretty_result("Get Weather", call_result.data)

            elif choice == '2':
                # --- Get Time ---
                timezone_input = input("Enter a timezone (e.g., America/New_York, Asia/Kolkata, Europe/London): ")
                if not timezone_input:
                    timezone_input = "UTC" # Default if user enters nothing
                print(f"Calling get_time for {timezone_input}...")
                call_result = await client.call_tool(
                    "get_time", 
                    {"timezone": timezone_input}
                )
                # The get_time tool now always returns a string
                result_str = call_result.data
                if result_str.startswith("Error:"):
                    print_pretty_result("Get Time", {"error": result_str})
                else:
                    print_pretty_result("Get Time", {"time": result_str})


            elif choice == '3':
                # --- Calculate ---
                expression_input = input("Enter a mathematical expression (e.g., 10 + 5 * 2): ")
                print(f"Calling calculate for '{expression_input}'...")
                call_result = await client.call_tool(
                    "calculate", 
                    {"expression": expression_input}
                )
                if call_result.is_error:
                    print_pretty_result("Calculate", {"error": call_result.data["error"]})
                else:
                    print_pretty_result("Calculate", call_result.data)

            elif choice == '4':
                print("Exiting client.")
                break
            
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    asyncio.run(main())
