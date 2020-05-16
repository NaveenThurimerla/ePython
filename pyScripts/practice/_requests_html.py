import requests

url = "https://blog.nen10.com"
response = requests.get(url)

print(response.content)