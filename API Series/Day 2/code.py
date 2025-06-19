# GET Request (fetching data from public API)
import requests

url = "https://jsonplaceholder.typicode.com/posts"
# response = requests.get(url)

# print("Status Code: ", response.status_code)
# print("Response JSON: ", response.json())


# POST Request (Sending data to API)
data = {
    "title": "API Learning",
    "body": "Let's learn and apply API",
    "userID": 1
}

response = requests.post(url, json=data)
print("Status COde: ", response.status_code)
print("Response JSON: ", response.json())