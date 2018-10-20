from django.db import models

# Create your models here.
class Company_details(models.Model):
	company_name = models.CharField(max_length = 60)
	company_email = models.CharField(max_length = 60)
	company_id = models.IntegerField()
	company_phn = models.CharField(max_length = 10)
	company_city = models.CharField(max_length = 60)


class Job_details(models.Model):
	job_id = models.IntegerField()
	job_name = models.CharField(max_length = 60)
	job_location = models.CharField(max_length = 60)
	job_position = models.CharField(max_length = 60)
	company_details = models.ForeignKey('Company_details', related_name='jobs')

class Question_details(models.Model):
	question_name = models.CharField(max_length = 60)
	question_model_answer = models.CharField(max_length = 100)
	question_id = models.IntegerField()
	question_type = models.CharField(max_length = 60)
	job_details = models.ForeignKey('Job_details', related_name='questions')

