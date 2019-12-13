from django.shortcuts import render
from django.http import HttpResponse
from .forms import NameForm
def index(request):
	return HttpResponse("Hello world.You are at the polls index")

def detail(request,question_id):
	return HttpResponse("You are looking at question %s." % question_id)

def results(request,question_id):
	response = "You are looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request,question_id):
	return HttpResponse("You are voting on question %s." % question_id)

def index(request):
	return render(request,'polls/index.html')

import datetime
def index(request):
	current_date_time=datetime.datetime.now()
	context={'now_date':current_date_time}
	return render(request,'polls/index.html',context)

def get_name(request):
	if request.method == "POST":
		form=NameForm(request.POST)
		if form.is_valid():
			return HttpResponse('Form submitted successfully<br>Name:'+form.cleaned_data['your_name'])
	else:
		form=NameForm()
	return render(request,'name.html',{'form':form})


# Create your views here.
