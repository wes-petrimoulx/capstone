import requests

######## Retrieves report on file by some type of referece/resource ########

# Link to the version 2 VirusTotal api that we will pull from
val = "373e7a863a1a345c60edb9e20ec32311"

def hashFileReport(r):
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey': '006da2c55d12a0a9748e7038ca83fef06fc390070027a054a121bc78fff8d5a4', 'resource': r}
    response = requests.get(url, params=params)
    print(response.json())

test(val)



def userFileReport(userfile):

	urlScan = 'https://www.virustotal.com/vtapi/v3/file/scan'
	paramsForUpload = {'apikey': '4f4679073ab77a95246bee964fc6016b939b4e9e0d66149180745c02f8a646e5'}
	files = {'file': (userfile, open(userfile, 'rb'))}
	userFileResponse = requests.post(urlScan, files=files, params=paramsForUpload)

	print(userFileResponse.json())






