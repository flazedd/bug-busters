import requests

# Proxy details
proxy = {
    'http': 'http://flzdd:yCfrcRzy9LTVf@ddc.oxylabs.io:8003',
    'https': 'https://flzdd:yCfrcRzy9LTVf@ddc.oxylabs.io:8003'
}

# URL to access
url = 'https://ip.oxylabs.io/location'

# Make a request using the proxy
response = requests.get(url, proxies=proxy)

# Print the response
print(response.text)
