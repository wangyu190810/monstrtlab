from django.shortcuts import render_to_response

from models import ordinaryUser



# Create your views here.

def ordinaryuser(request):
    error=[]
    return render_to_response('user.html')

