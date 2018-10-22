from django.shortcuts import render

# Create your views here.
def homepage(request):
	return render(request, 'home/index.html')

def aboutpage(request):
	return render(request, 'home/about-us.html')