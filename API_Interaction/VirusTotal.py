import requests
#import vt
import json


######## Retrieves report on file by some type of referece/resource ########


currentReport = ""
# Link to the version 2 VirusTotal api that we will pull from
val = "373e7a863a1a345c60edb9e20ec32311"

# Returns report for file based on file hash
def hashFileReport(r):
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey': '006da2c55d12a0a9748e7038ca83fef06fc390070027a054a121bc78fff8d5a4', 'resource': r}
    response = requests.get(url, params=params)

    return response.json()

# Returns report for file based on user end file location
def userFileReport(userfile):
	urlScan = 'https://www.virustotal.com/vtapi/v3/file/scan'
	paramsForUpload = {'apikey': '4f4679073ab77a95246bee964fc6016b939b4e9e0d66149180745c02f8a646e5'}
	files = {'file': (userfile, open(userfile, 'rb'))}
	userFileResponse = requests.post(urlScan, files=files, params=paramsForUpload)
	
	return userFileResponse.json()

# These are all functions to GET specific info by file hash
def get_md5(hash):
	json_report = hashFileReport(hash)
	md5 = json_report["md5"]
	return md5

def get_sha256(hash):
	json_report = hashFileReport(hash)
	sha256 = json_report["sha256"]
	return sha256

def get_sha1(hash):
	json_report = hashFileReport(hash)
	sha1 = json_report["sha1"]
	return sha1

def get_scanDate(hash):
	json_report = hashFileReport(hash)
	scan_date = json_report["scan_date"]
	return scan_date

def get_pos(hash):
	json_report = hashFileReport(hash)
	pos = json_report["positives"]
	return pos

def get_total(hash):
	json_report = hashFileReport(hash)
	total = json_report["total"]
	return total

def get_permalink(hash):
	json_report = hashFileReport(hash)
	permalink = json_report["permalink"]
	return permalink

# These are all functions to GET specific info by user file upload
def get_md5_upload(userFile):
	json_report = hashFileReport(userFile)
	md5 = json_report["md5"]
	return md5

def get_sha256_upload(userFile):
	json_report = hashFileReport(userFile)
	sha256 = json_report["sha256"]
	return sha256

def get_sha1_upload(hash):
	json_report = userFileReport(userfile)
	sha1 = json_report["sha1"]
	return sha1

def get_scanDate_upload(userFile):
	json_report = userFileReport(userfile)
	scan_date = json_report["scan_date"]
	return scan_date

def get_pos_upload(userFile):
	json_report = userFileReport(userfile)
	pos = json_report["positives"]
	return pos

def get_total_upload(userFile):
	json_report = userFileReport(userfile)
	total = json_report["total"]
	return total

def createTextFile(data, fileName):
	save_path = 'Malware_GUI\Malware_GUI\Data'
	complete_path = save_path + fileName
	fh = open(complete_path,'w')
	fh.write(str(data))
	fh.close()
	print(fileName + " created")

# Reads the file that conatins the hash value from the user
# hashVal = str(open("string.txt", "r"))
hashVal = "79dd810d875c1f0fbd89f2ae5191f9dcb209e4445a1c1c8442a7875ad89d82e1"


# Text file creation
# We can only pull 4 at a time

# createTextFile(get_md5(hashVal), "md5")

#createTextFile(get_sha256(hashVal),"\sha256")

# createTextFile(get_sha1(hashVal),"sha1")

# createTextFile(get_scanDate(hashVal),"scanDate")

#createTextFile(get_permalink(hashVal),"\permalink")

#createTextFile(get_pos(hashVal),"\positives")

createTextFile(get_total(hashVal),"\total")



# manual tests 
# hashFileReport test
"""
val = "373e7a863a1a345c60edb9e20ec32311" # random hash
print(hashFileReport(val))
"""



