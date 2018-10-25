from django.shortcuts import render
from company.models import Company_details,Job_details

# Create your views here.
def canhomepage(request):
	companies = Company_details.objects.all()
	print(companies)
	return render(request,'candidate/index.html',{'companies':companies})

def sendComp(request,ide):
    if request.method == 'POST':
        j = Company_details(company_name=id)
        print(j.company_name)
        jobs = Job_details.objects.get(company=j.company_name)
        print(jobs)
    return render(request,'candidate/jobs.html',{'jobs':jobs})

