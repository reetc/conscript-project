from django.contrib import admin

# Register your models here.



from company.models import Company_details, Job_details, Question_details

# Register your models here.
admin.site.register(Company_details)
admin.site.register(Job_details)
admin.site.register(Question_details)
