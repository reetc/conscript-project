
# Create your models here.
# class Company_details(models.Model):
# 	company_name = models.CharField(max_length = 60)
# 	company_email = models.CharField(max_length = 60)
# 	# company_id = models.AutoField(primary_key=True,default=0)
# 	company_phn = models.CharField(max_length = 10)
# 	company_city = models.CharField(max_length = 60)
#
# 	def __str__(self):
# 		return "%s" %(self.company_name)




from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Company_details(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE,default="",blank=True,null=True)
	company_name = models.TextField(max_length=500)
	company_location = models.CharField(max_length=30, blank=True)
	company_email = models.CharField(max_length=60)


	def __str__(self):
		return "%s" %(self.company_name)
#
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


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
