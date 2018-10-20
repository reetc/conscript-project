from django.db import models

# Create your models here.
class Candidate_personal_details(models.Model):
	candidate_name = models.CharField(max_length = 60)
	candidate_email = models.CharField(max_length = 60)
	candidate_id = models.IntegerField()
	candidate_age = models.IntegerField()

class Job_application_details(models.Model):

	company_name = models.CharField(max_length = 60)
	job_location = models.CharField(max_length = 60)
	job_position = models.CharField(max_length = 60)
	candidate_id_foreign = models.ForeignKey(Candidate_personal_details, on_delete= models.CASCADE)
