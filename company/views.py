from django.shortcuts import render
from .models import Job_details
from .models import Company_details
from .models import Question_details
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect



# Create your views here.

# @login_required
def admin_dashboard(request):
	# if(request.user.company_details.company_name == 'GHI'):
	# 	return redirect('canhome')
	# else:
		return render(request, 'company/index.html')



def register_company(request):
	if request.method == 'POST':

		user=User()
		company=Company_details()
		user = User.objects.create_user(username=request.POST['username'],password=request.POST['password'])
		# user.username=request.POST['username']
		# user.password=user.set_password('password')
		user.save()
		# user.Company_details.company_name=request.POST['company_name']
		company.user=User.objects.get(username=request.POST['username'])
		company.company_name=request.POST['company_name']
		# user.Company_details.company_location="Bangalore"
		company.company_location="Bangalore"
		# user.Company_details.company_email="efg@gmail.com"
		company.company_email="efg@gmail.com"
		# user.save()
		company.save()

		previous_page = request.META['HTTP_REFERER']
		data = {'previous_page': previous_page,'abc': 56}
		return render(request,'company/register_company.html',data)
	else:
		previous_page = request.META['HTTP_REFERER']
		data = {'previous_page': previous_page,'abc': 56}
		return render(request,'company/register_company.html',data)


def interview_list(request):
	return render(request, 'company/interviewList.html')

def invite(request):
    return render(request, 'company/invite.html')

def domains(request):
	if request.method == 'POST':

		job=Job_details()
		job.job_name = request.POST['job_name']
		job.job_location = request.POST['job_location']
		job.job_position = request.POST['job_position']
		company_n=request.user.company_details.company_name
		job.company=Company_details.objects.get(company_name=company_n)
		job.save()

		question=Question_details()
		question.question_name = request.POST['question']
		question.model_answer = request.POST['sample_answer']
		question.question_type = request.POST['question_type']
		question.time_limit = int(request.POST['time_limit'])
		question.job = job
		question.save()



		previous_page = request.META['HTTP_REFERER']
		data = {'previous_page': previous_page,'abc': 56}
		return render(request,'company/domains.html',data)
	else:
		previous_page = request.META['HTTP_REFERER']
		data = {'previous_page': previous_page,'abc': 56}
		return render(request,'company/domains.html',data)
