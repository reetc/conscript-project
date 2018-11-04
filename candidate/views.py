from django.shortcuts import render
from company.models import Company_details,Job_details
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def canhomepage(request):
	companies = Company_details.objects.all()
	print(companies)
	return render(request,'candidate/index.html',{'companies':companies})

def sendComp(request,ide):
    if request.method == 'POST':
        jobs = Job_details.objects.filter(company_id=ide)
        print(jobs)
        return render(request,'candidate/jobs.html',{'jobs':jobs})
    else:
    	return render(request, 'candidate/jobs.html')

def questions(request):
	return render(request, 'candidate/first.html')


def webcam(request):
	return render(request, 'candidate/webcam.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        name = request.POST.get('name')
        user = User.objects.create(
            first_name = name,
            username = username,
            )
        user.set_password(password)
        user.save()

        user = authenticate(username = username, password = password)
        login(request, user)
        return redirect('/candidate/canhomepage/')
    else:
        return render(request,'candidate/register.html')   

def login_blog(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user :
            if user.is_active:
                login(request,user)
                return redirect('/candidate/canhomepage/')
            else:
                return HttpResponse('Disabled Account')
        else:
            return HttpResponse("Invalid Login details.Are you trying to Sign up?")
    else:
        return render(request,'candidate/login.html')

def logout_blog(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request,'candidate/logout.html')
    else:
        return HttpResponseRedirect('/login/')