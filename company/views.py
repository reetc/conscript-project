from django.shortcuts import render
from .models import Job_details
from .models import Company_details
from .models import Question_details
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from . import functs
from candidate.models import Job_application_details

from django.contrib.auth import authenticate, login, logout


from candidate.models import Emotion_output
from candidate.models import Sentiment_output
from candidate.models import Similarity_output

# Create your views here.

# @login_required
def admin_dashboard(request):
	# if(request.user.company_details.company_name == 'GHI'):
	# 	return redirect('canhome')
	# else:
		return render(request, 'company/index.html')



def com_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user :
            if user.is_active:
                login(request,user)
                return redirect('/company/admin_dashboard/')
            else:
                return HttpResponse('Disabled Account')
        else:
            return HttpResponse("Invalid Login details.Are you trying to Sign up?")
    else:
        return render(request,'company/login.html')



def analysis(request):
	data_emo = Emotion_output.objects.all()
	data_sentiment = Sentiment_output.objects.all()
	data_similarity = Similarity_output.objects.all()
	emo = {
    'emotion': data_emo
	}

	senti = {
	'sentiment': data_sentiment
	}

	simi = {
	'similarity': data_similarity
	}

	# print()
	# print()
	# print()
	# print()
	# print()
	# print(data_emo)
	# print()
	# print()
	# print()
	# print()
	# print()
	# # for d in emo:
	# # 	print(d.data_emo)
	# print('holaaa')
	# for d in data_emo:
	# 	print(d.emo_output)
	# print('yo')
	# print(emo['emotion'])
	return render(request, "company/analysis.html", context={"emo": emo, "senti": senti, "simi":simi})


def display_results(request):
	this_company=request.user.company_details
	jobs_list=Job_details.objects.filter(company = this_company)
	if jobs_list:
		selected_job=jobs_list.filter(job_name = "Software Developer")
		if selected_job:
			job_questions_objects=Question_details.objects.filter(job = selected_job[0])
			job_questions=job_questions_objects.values('question_name')[0].get('question_name')
			model_answer=job_questions_objects.values('model_answer')[0].get('model_answer')
			# model_answer=job_questions.values('model_answer')[0].get('model_answer')
			# job_questions=job_questions_object.question_name



			relevance=functs.answer_relevance(request)
			data = {'previous_page': "previous_page",'relevance': relevance,'job_list': jobs_list,'job':selected_job,'job_questions':job_questions,'model_answer':model_answer}
			return render(request,'company/results.html',data)
		else:
			return HttpResponse("No Software Development Job Posted", content_type="text/plain")
	else:
		return HttpResponse("No Job Posted", content_type="text/plain")



def application_result(request,id):
	return HttpResponse("No Job Posted", content_type="text/plain")



def applications_list(request):
	this_company_name=request.user.company_details.company_name
	applications = Job_application_details.objects.filter(company_name = this_company_name)
	return render(request, 'company/applicationsList.html',{'applications':applications})


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
		company.company_location="Mumbai"
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
