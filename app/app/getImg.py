import urllib
import requests
import json
import ast
import thread
import time
from login import face_recognizer

acessToken = '12~xaUyASKJkoRdNxBRvVAO3nBcGxHUtBB04DsALbOcpG3ITKVF4B0HwgAHHiKp9ruH'

def getStudents():
    r = requests.get("https://sjsu.instructure.com/api/v1/courses/1204953/students?access_token="+acessToken );
    # r = "{ 'list' : " + r.content + " }"
    r = r.content.replace("{","'{")
    r = r.replace("}","}'")
    r = ast.literal_eval(r)
    data =[]
    for i in r:
    	i = json.loads(i)
    	data.append(i)
    	# print i['name']

    print len(data)
    getImg(data)
    # data  = json.loads(r)
    # print data
    return data

def getImg(data):
	# url = "https://sjsu.instructure.com/images/users/4199629?access_token=12~B8z59M1BUWZzpF4Ynfeu7rORyOxCmKzpMCYajrhYKEgc6e0U6vtGUDhsmfXAg3ia"
    # urllib.urlretrieve(url, "demo.png")
    # i = 0
 	for s in data:
 		# i=i+1
 		id = str(s['id'])
 		# id = s['name']+'-'+id
 		filename = "temp/"+id+".png"
 		# print filename
 		url = "https://sjsu.instructure.com/images/users/"+ id+"?access_token="+acessToken
   		# thread.start_new_thread( saveImg, (url, filename) )
   		

 	print "end"
 		# print url
    	# break 
 		# 	testfile = urllib.URLopener()
		# testfile.retrieve(url, filename)
		# # f = open(filename,'wb')
		# # f.write(requests.get(url).content)
		# # f.close()
		# try:
	 	#        urllib.urlretrieve(url,filename)
	 	#    except:
	 	#        print "save failed" 
    	# urllib.urlretrieve(url, filename)
    	# if i>=3: 

def saveImg(url,filename):
	urllib.urlretrieve(url, filename)
	print filename














