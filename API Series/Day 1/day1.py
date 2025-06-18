# Call a real public API
import requests  # Library for API Call  to make HTTP request

url = "https://catfact.ninja/fact"     # Define the API URL (endpoint) - we want to call

response = requests.get(url)           # Send GET request to the API  - It fetches the data

data = response.json()                 # Convert response to JSON (dict in Python)

print("Cat Fact:", data['fact'])
