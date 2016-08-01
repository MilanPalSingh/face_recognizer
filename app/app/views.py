from django.shortcuts import render
# from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
# from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponse
# SAHIL: comment this 
from login import face_recognizer

# Create your views here.

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
    # u = request.GET['user']
    # print u
    return render_to_response(
    # face_recognizer.init()
    'profile.html',
    { 'user': '3' }
    )# Create your views here.

def submit(request):
    print "request.img"
    imgUri = request.GET['img']
    print imgUri
    # user = 3
    # SAHIL: comment this 
    user = face_recognizer.startAppWithImg(imgUri)
    print user
    return HttpResponseRedirect('/profile/',{'user': user})






