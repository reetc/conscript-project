from django.shortcuts import render

# Create your views here.
def admin_dashboard(request):
	return render(request, 'company/index.html')

def interview_list(request):
	return render(request, 'company/interviewList.html')

def invite(request):
    return render(request, 'company/invite.html')

def domains(request):
    return render(request, 'company/domains.html')




