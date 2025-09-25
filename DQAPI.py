import requests

endpoint_url = 'https://api.exchangerate-api.com/v4/latest/usd'

# Make a GET request to the API endpoint
response = requests.get(endpoint_url)
response_dict = response.json()

print(type(response))
print(type(response_dict))

print(response_dict["rates"])

print(response_dict["rates"])