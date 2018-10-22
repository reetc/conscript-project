from django.shortcuts import render

# Create your views here.
def canhomepage(request):
	return render(request, 'candidate/index.html')