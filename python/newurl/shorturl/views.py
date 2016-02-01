from django.shortcuts import render
from .models import Entry
from django.shortcuts import get_object_or_404, render
import base64
from django.http import HttpResponseRedirect
import re

def make_short(request):
	context = {}
	return render(request, 'shorturl/shorturl.html',context)

def change(request):
	old_url= request.POST['original_url']
	if not re.search('//',old_url):
		return render(request,'shorturl/invalidentry.html',)
	
	else: 
		base64_url = base64.urlsafe_b64encode(old_url)
		entry = Entry(original_url=old_url, new_url=base64_url)
		entry.save()
		context= {"new_url":base64_url}

		return render(request, 'shorturl/changedurl.html',context)

def original(request, new_url):
	entry = Entry.objects.get(new_url=new_url)
	old_url = entry.original_url
	print new_url
	return HttpResponseRedirect(old_url)

