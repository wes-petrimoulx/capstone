import requests

url = 'https://www.virustotal.com/vtapi/v2/file/report'

params = {'apikey': '4f4679073ab77a95246bee964fc6016b939b4e9e0d66149180745c02f8a646e5', 'resource': '<resource>'}

response = requests.get(url, params=params)

print(response.json())