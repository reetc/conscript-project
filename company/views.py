from django.shortcuts import render

# Create your views here.
def candidate_list(request):
	return render(request, 'company/index.html')

def interview_list(request):
	return render(request, 'company/interviewList.html')