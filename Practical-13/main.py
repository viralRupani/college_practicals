# Install urllib3 package using PIP. Send HTTP requests to any URL
# and print status for the same


# pip install urllib3
import urllib3

http = urllib3.PoolManager()
response = http.request('GET', 'https://www.python.org/')
print(response.status)