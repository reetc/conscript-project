from django.contrib import admin

# Register your models here.
from candidate.models import Candidate_personal_details, Job_application_details

# Register your models here.
admin.site.register(Candidate_personal_details)
admin.site.register(Job_application_details)
