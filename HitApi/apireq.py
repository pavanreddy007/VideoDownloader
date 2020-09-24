import requests

URL="http://127.0.0.1:8000/Youtube/download"

file1={'file':open('video1.txt','r')}
x=requests.post(url=URL,data=file1)

if (x.status_code==200):

	print("video is downloaded")

else:
	print("please check internet connection or there is problem in input Text file")
 