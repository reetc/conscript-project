from django.shortcuts import render
from .models import Job_details
from .models import Company_details
from .models import Question_details
from django.template import RequestContext
from django.http import HttpResponseRedirect
# Create your views here.
def admin_dashboard(request):
	return render(request, 'company/index.html')

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
		job.company=Company_details.objects.get(company_name="DEF")
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
