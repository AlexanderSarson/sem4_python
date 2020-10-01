import requests

# url = "http://api.openweathermap.org/data/2.5/forecast"
# req = requests.get(url, params={'q': 'Copenhagen,dk',
#                                 'mode': 'json',
#                                 'units': 'metric',
#                                 'appid': "389b334a42c11f69464cf7ad0fd4d7e1"})

url = "https://www.gutenberg.org/files/1342/1342-0.txt"
req = requests.get(url)
response = req.text
print(response)
# req_json = json.loads(req.text)

# print(req_json)
