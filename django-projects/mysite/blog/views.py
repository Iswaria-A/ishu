import csv
from blog.models import Blog,Images
from blog.forms import BlogForm,SignupForm,LoginForm,UploadFileForm
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.http import JsonResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import(
	HTTP_400_BAD_REQUEST,
	HTTP_404_NOT_FOUND,
	HTTP_200_OK
	)
from rest_framework.response import Response
from rest_framework import permissions
from blog.serializers import BlogSerializers
from rest_framework import status





def insert_blog(request):
	if request.method=='POST':
		blog_form=BlogForm(request.POST)
		if blog_form.is_valid():
			blog_name_from_user=blog_form.cleaned_data['blog_name']
			blog_tagline_from_user=blog_form.cleaned_data['blog_tag_line']
			blog_object=Blog(name=blog_name_from_user,tagline=blog_tagline_from_user)
			blog_object.save()
			return HttpResponse('Data Inserted Successfully')
	else:
		blog_form=BlogForm()
		return render(request,'insert.html',{'form':blog_form})

# Create your views here.
def showBlog(request,requested_blog_id):
	blog_details=Blog.objects.get(id=requested_blog_id)
	context={"blog":blog_details}
	return render(request,"view-blog.html",context)



def edit_blog(request,requested_blog_id):
	if request.method == 'POST':
		blog_form=BlogForm(request.POST)
		if blog_form.is_valid():
			blog_details=Blog.objects.get(id=requested_blog_id)
			blog_details.name=blog_form.cleaned_data['blog_name']
			blog_details.tagline=blog_form.cleaned_data['blog_tag_line']
			blog_details.save()
		return HttpResponse('Data Edited Successfully')
	else:
		blog_details=Blog.objects.get(id=requested_blog_id)
		blog_form=BlogForm(initial={"blog_name":blog_details.name,"blog_tag_line":blog_details.tagline})
	return render(request,'edit-blog.html',{'form':blog_form,'blog_id':requested_blog_id})


def delete_entry(request,requested_blog_id):
	blog_details=Blog.objects.get(id=requested_blog_id)
	blog_details.delete()
	return HttpResponse('Data Deleted Successfully')

def listBlogs(request):
	blogs_list=Blog.objects.all()
	paginator=Paginator(blogs_list,2)
	page=request.GET.get('page')
	blogs=paginator.get_page(page)
	return render(request,"blog/list-blogs.html",{"blogs":blogs})

def signup(request):
	if request.method=='POST':
		signup_form=SignupForm(request.POST)
		if signup_form.is_valid():
			username=signup_form.cleaned_data['username']
			email=signup_form.cleaned_data['email']
			password=signup_form.cleaned_data['password']
			if User.objects.filter(username=username).exists():
				return HttpResponse("Username/email already exists")
			else:
				user=User.objects.create_user(username,email,password)
				user.save()
				return HttpResponse("Signup Successfull")
	else:
		signup_form=SignupForm(request.POST)
	return render(request,'blog/signup.html',{"form":signup_form})

def logined(request):
	if request.user.is_authenticated:
		return HttpResponse("You are already logged in")
	else:
		if request.method=='POST':
			login_form=LoginForm(request.POST)
			if login_form.is_valid():
				username=login_form.cleaned_data['username']
				password=login_form.cleaned_data['password']
				user=authenticate(username=username,password=password)
				if user is not None:
					if user.is_active:
						login(request,user)
						return HttpResponse('Login Successfull')
					else:
						return HttpResponse('Your Account is not active')
				else:
					return HttpResponse('The Account does not exist')

		else:
			login_form=LoginForm()
			messages.add_message(request,messages.SUCCESS,'Successfully Added')


			return render(request,"blog/login.html",{"form":login_form})
def logout_view(request):
	logout(request)
	return HttpResponse('loggedout Successfully')



def index(request):
	messages.error(request,'Document Deleted')
	return render(request,'blog/index.html')

def sample_view(request):
	if request.method=='POST':
		signup_form=SignupForm(request.POST)
		if signup_form.is_valid():
			username=signup_form.cleaned_data['username']
			email=signup_form.cleaned_data['email']
			password=signup_form.cleaned_data['password']
			if User.objects.filter(username=username).exists():
				return HttpResponse("Username/email already exists")
			else:
				user=User.objects.create_user(username,email,password)
				user.save()
				return HttpResponseRedirect('/blog/login')
	else:
		signup_form=SignupForm(request.POST)
	return render(request,'blog/signup.html',{"form":signup_form})


def upload_file(request):
	if request.method=='POST':
		form=UploadFileForm(request.POST,request.FILES)
		if form.is_valid():
			instance=Images(image=request.FILES['image'])
			instance.save()
			messages.add_message(request,messages.SUCCESS,'Successfully Added')
			return HttpResponseRedirect('/blog/login')
	else:
		form=UploadFileForm()
		return render(request,'blog/upload.html',{'form':form})

def showImage(request):
	img=Images.objects.get(id=1)
	return render(request,'polls/image_preview.html',{"file":img})

def sendMailToUser(request):
	subject = "Invitation"
	message = "Welcome to the party"
	sender = "iswaria1995@gmail.com"
	receivers = ["iswaria1995@gmail.com"]
	msg = EmailMessage(subject,message,sender,receivers)
	msg.content_subtype = "html"
	msg.attach_file('/Mashupstack/css/nat3.jpg')
	msg.send()
	return HttpResponse("send mail")

def sample_view(request):
	return render(request,"blog/ajax_template.html")

def some_view(request):
	response=HttpResponse(content_type='text/csv')
	response['Content-Disposition']='attachment;filename="somefilename.csv"'
	writer=csv.writer(response)
	writer.writerow(['First row','Foo','Bar','Baz'])
	writer.writerow(['Second row','A','B','C','"Testing"',"Heres a quote"])
	return response

def html_to_pdf_view(request):
	blog_objects=Blog.objects.all()
	template_path='blog/pdf_template.html'
	context={"blogs":blog_objects}
	response=HttpResponse(content_type='application/pdf')
	response['Content-Disposition']='attachment;filename="report.pdf"'
	template=get_template(template_path)
	html=template.render(context)
	pisaStatus=pisa.CreatePDF(html,dest=response,link_callback="")
	if pisaStatus.err:
		return HttpResponse('We had some errors <pre>' + html + '</pre>')
	return response


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
	username = request.data.get("username")
	password = request.data.get("password")
	if username is None or password is None:
		return Response({'error':'Please provide both username and password'},
			status=HTTP_400_BAD_REQUEST)
	user=authenticate(username=username,password=password)
	if not user:
		return Response({'error':'Invalid Credentials'},
			status=HTTP_404_NOT_FOUND)
	token,_= Token.objects.get_or_create(user=user)
	return Response({'token':token.key},
		status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
@permission_classes((permissions.AllowAny,))

def sample_api(request):
	data={"message":"Hello World"}
	return Response(data,status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def sample_data(request):
	blogs=Blog.objects.all()
	serializer=BlogSerializers(blogs,many=True)
	return Response(serializer.data)


@csrf_exempt
@api_view(["PUT"])
@permission_classes((permissions.AllowAny,))
def sample_put(request,blog_id):
	blog=Blog.objects.get(id=blog_id)
	serializer=BlogSerializers(blog,data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)
	return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(["DELETE"])
@permission_classes((permissions.AllowAny,))
def sample_delete(request,blog_id):
	blog=Blog.objects.get(id=blog_id)
	blog.delete()
	return Response(status=status.HTTP_204_NO_CONTENT)