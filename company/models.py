from django.db import models

# Create your models here.
class Company_details(models.Model):
	company_name = models.CharField(max_length = 60)
	company_email = models.CharField(max_length = 60)
	# company_id = models.AutoField(primary_key=True,default=0)
	company_phn = models.CharField(max_length = 10)
	company_city = models.CharField(max_length = 60)

	def __str__(self):
		return "%s" %(self.company_name)


class Job_details(models.Model):
	# job_id = models.AutoField(primary_key=True,default=0)
	job_name = models.CharField(max_length = 60)
	job_location = models.CharField(max_length = 60)
	job_position = models.CharField(max_length = 60)
	company = models.ForeignKey('Company_details', related_name='jobs',on_delete= models.CASCADE)

	def __str__(self):
		return "%s" %(self.job_name)



class Question_details(models.Model):
	question_name = models.CharField(max_length = 60)
	model_answer = models.CharField(max_length = 100)
	# question_id = models.AutoField(primary_key=True,default=0)
	question_type = models.CharField(max_length = 60)
	job = models.ForeignKey('Job_details', related_name='questions',on_delete= models.CASCADE)
	time_limit=models.IntegerField(default=3)
