import sys
print(sys.executable)

import requests
import json

# Prompt the user for the file path
file_path = input("Enter the path to your CSV file: ")

# Define the API endpoint
api_url = "http://127.0.0.1:5000/upload"  # Update if API is hosted elsewhere

try:
    # Open the file and send it to the API
    with open(file_path, 'rb') as file:
        response = requests.post(api_url, files={'file': file})

    # Check if the request was successful
    if response.status_code == 200:
        # Parse and print the JSON response
        data = response.json()
        print("\n=== Summary ===")
        print(json.dumps(data["summary"], indent=4))
        print("\n=== Transactions ===")
        for transaction in data["data"]:
            print(json.dumps(transaction, indent=4))
    else:
        # Print error message from the API
        print(f"Error: {response.status_code} - {response.text}")

except FileNotFoundError:
    print("Error: File not found. Please check the file path and try again.")
except requests.exceptions.RequestException as e:
    print(f"Error: Unable to connect to the API. Details: {e}")
