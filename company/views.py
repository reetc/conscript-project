from django.shortcuts import render

# Create your views here.
def comhomepage(request):
	return render(request, 'company/index.html')