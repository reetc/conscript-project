from django.shortcuts import render

# Create your views here.
def homepage(request):
	return render(request, 'home/index.html')

def aboutpage(request):
	return render(request, 'home/about-us.html')

def portal(request):
	return render(request, 'home/portal.html')

def contactpage(request):
	return render(request, 'home/contact-us.html')

def blog(request):
	return render(request, 'home/blog-post-list.html')


