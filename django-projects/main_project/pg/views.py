from django.shortcuts import render

def home(request):
	return render(request,'pg/index.html')

# Create your views here.
