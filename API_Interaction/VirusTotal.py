import requests

######## Retrieves report on file by some type of referece/resource ########

# Link to the version 2 VirusTotal api that we will pull from
url = 'https://www.virustotal.com/vtapi/v2/file/report'

# The resource argument can be the MD5, SHA-1 or SHA-256 of a file for which you want to retrieve the most recent antivirus report. 
# You may also specify a scan_id returned by the /file/scan endpoint.
params = {'apikey': '4f4679073ab77a95246bee964fc6016b939b4e9e0d66149180745c02f8a646e5', 'resource': '<resource>'}


response = requests.get(url, params=params)

#Currently just prints outs entire report
print(response.json())


# retrieve report converted into a method
def retrieveReport(r):
	r = resource
	params = {'apikey': '4f4679073ab77a95246bee964fc6016b939b4e9e0d66149180745c02f8a646e5', 'resource': r}
	url = 'https://www.virustotal.com/vtapi/v2/file/report'
	response = requests.get(url, params = params)
	print(response)


######## Uploads a user file, then responds with report ######## 

urlScan = 'https://www.virustotal.com/vtapi/v2/file/scan'

paramsForUpload = {'apikey': '4f4679073ab77a95246bee964fc6016b939b4e9e0d66149180745c02f8a646e5'}

files = {'file': ('myfile.exe', open('myfile.exe', 'rb'))}

userFileResponse = requests.post(urlScan, files=files, params=paramsForUpload)

print(userFileResponse.json())

