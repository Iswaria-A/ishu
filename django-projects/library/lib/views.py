from django.shortcuts import render
from django.http import HttpResponse
from lib.forms import AddForm
from lib.models import books
from django.http import HttpResponseRedirect

def intro(request):
	book_details=books.objects.all()
	context={"lib":book_details}
	return render(request,'lib/index.html',context)

def add_books(request):
	if request.method=='POST':
		lib_form=AddForm(request.POST)
		if lib_form.is_valid():
			lib_name_from_user=lib_form.cleaned_data['lib_name']
			lib_authorname_from_user=lib_form.cleaned_data['lib_author_name']
			lib_year_from_user=lib_form.cleaned_data['lib_year']
			lib_price_from_user=lib_form.cleaned_data['lib_price']
			lib_object=books(name=lib_name_from_user,author_name=lib_authorname_from_user,year=lib_year_from_user,price=lib_price_from_user)
			lib_object.save()
			return HttpResponseRedirect('/lib/first')
	else:
		lib_form=AddForm()
		return render(request,'lib/add.html',{'form':lib_form})


def view_books(request,book_id):
	view_details=books.objects.get(id=book_id)
	context={"book":view_details}
	return render(request,'lib/view.html',context)

def edit_books(request,book_id):
	if request.method=='POST':
		lib_form=AddForm(request.POST)
		if lib_form.is_valid():
			lib_details=books.objects.get(id=book_id)
			lib_details.name=lib_form.cleaned_data['lib_name']
			lib_details.author_name=lib_form.cleaned_data['lib_author_name']
			lib_details.year=lib_form.cleaned_data['lib_year']
			lib_details.price=lib_form.cleaned_data['lib_price']
			lib_details.save()
			return HttpResponseRedirect('/lib/first')
	else:
		lib_details=books.objects.get(id=book_id)
		lib_form=AddForm(initial={"lib_name":lib_details.name,"lib_author_name":lib_details.author_name,"lib_year":lib_details.year,"lib_price":lib_details.price})
	return render(request,'lib/edit.html',{'form':lib_form,'lib_id':book_id})

def delete_books(request,book_id):
	lib_details=books.objects.get(id=book_id)
	lib_details.delete()
	return HttpResponseRedirect('/lib/first')

# Create your views here.
