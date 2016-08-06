from django.shortcuts import render
# from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
# from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponse
import requests
# SAHIL: comment this 
from login import face_recognizer
from linkedin import linkedin
# Create your views here.
import urllib
from app import getImg
import thread

# filename: path of the img, id: canvasID, user: faceRegSystemID
def matchID(filename, id , user ):
    flage  = face_recognizer.checkImg(filename)
    # if flag == 3:
    print filename +" - "+ str(flage) 

def getUserID(data, user):
    print len(data)
    itercars = iter(data)
    next(itercars)
    next(itercars)
    for s in itercars:
        # i=i+1
        id = str(s['id'])
        # id = s['name']+'-'+id
        filename = "temp/"+id+".png"
        # print filename
        thread.start_new_thread( matchID, (filename, id , user) )

# @login_required
def home(request):
    # execfile('login/test.py')
    # SAHIL: comment this 
    face_recognizer.init()
    #	print a
    return render_to_response(
    'home.html',
    { 'user': '3' }
    )# Create your views here.

def profile(request):
    # execfile('login/test.py')
    u = request.GET['user']
    print u
    return render_to_response('profile.html')# Create your views here.

def submit(request):
    print "request.img"
    # SAHIL: comment this 
    imgUri = request.GET['img']
    # SAHIL: comment this 
    # print imgUri
    # user = 3
    # SAHIL: comment this 
    r = getImg.getStudents()
    user = face_recognizer.startAppWithImg(imgUri)
    print user
    ID = getUserID(r,user)
    return HttpResponseRedirect('/profile/?user='+ str(user))

def auth(request):
    # execfile('login/test.py')
    # SAHIL: comment this 
    # face_recognizer.init()

    # RETURN_URL = 'http://127.0.0.1:8000/auth/'
    # token= 12~B8z59M1BUWZzpF4Ynfeu7rORyOxCmKzpMCYajrhYKEgc6e0U6vtGUDhsmfXAg3ia
    # r = requests.get('https://sjsu.instructure.com/api/v1/courses', headers={'Authorization': '2~B8z59M1BUWZzpF4Ynfeu7rORyOxCmKzpMCYajrhYKEgc6e0U6vtGUDhsmfXAg3ia'})
    # r = requests.get("https://sjsu.instructure.com/api/v1/courses/1204953/students?access_token=12~B8z59M1BUWZzpF4Ynfeu7rORyOxCmKzpMCYajrhYKEgc6e0U6vtGUDhsmfXAg3ia" );
    # https://sjsu.instructure.com/api/v1/courses/1204953/students?access_token=12~B8z59M1BUWZzpF4Ynfeu7rORyOxCmKzpMCYajrhYKEgc6e0U6vtGUDhsmfXAg3ia
    # 4199027
    # https://sjsu.instructure.com/api/v1/users/4199027?access_token=12~B8z59M1BUWZzpF4Ynfeu7rORyOxCmKzpMCYajrhYKEgc6e0U6vtGUDhsmfXAg3ia
    # https://sjsu.instructure.com/api/v1/files/43772967?access_token=12~B8z59M1BUWZzpF4Ynfeu7rORyOxCmKzpMCYajrhYKEgc6e0U6vtGUDhsmfXAg3ia
    # $.getJSON("https://sjsu.instructure.com/api/v1/courses?access_token=12~B8z59M1BUWZzpF4Ynfeu7rORyOxCmKzpMCYajrhYKEgc6e0U6vtGUDhsmfXAg3ia", function(data) { console.log(data.responseText); });
    r = getImg.getStudents()

    # print r.content 
    # https://sjsu.instructure.com/images/users/4199177?access_token=<access token>
    # urllib.urlretrieve ("https://sjsu.instructure.com/files/43772967/download?download_frd=1&verifier=pKEgWsx510W32CrpUddnDCoOdiEg1CvIm9B8poF9", "demo.png")
    # https://sjsu.instructure.com/files/43772967/download?download_frd=1&verifier=pKEgWsx510W32CrpUddnDCoOdiEg1CvIm9B8poF9
    # https://sjsu.instructure.com/files/43772967/download?download_frd=1&verifier=pKEgWsx510W32CrpUddnDCoOdiEg1CvIm9B8poF9

    return render_to_response(
    'auth.html',
    { 'user': '3' }
    )# Create your views here.








