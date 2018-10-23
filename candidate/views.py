from django.shortcuts import render
from company.models import Company_details

# Create your views here.
def canhomepage(request):
	companies = Company_details.objects.all()
	print(companies)
	return render(request,'candidate/index.html',{'companies':companies})


