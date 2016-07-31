from django.shortcuts import render
# from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
# from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponse
from login import face_recognizer

# Create your views here.

# @login_required
def home(request):
    # execfile('login/test.py')
    face_recognizer.init()
    #	print a
    return render_to_response(
    'home.html',
    { 'user': '3' }
    )# Create your views here.

def profile(request):
    # execfile('login/test.py')
    #	print a
    # face_recognizer.startApp()
    return render_to_response(
    # face_recognizer.init()
    'profile.html',
    { 'user': '3' }
    )# Create your views here.

def submitImg(request, imgUri):
    print imgUri
    return redirect('/profile/')
    