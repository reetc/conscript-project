from django.db import models
from django.contrib.postgres.fields import HStoreField
from jsonfield import JSONField

from company.models import Job_details
from django.utils.translation import gettext as _
import datetime
from django.contrib.auth.models import User


# Create your models here.
class Candidate_personal_details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default="",blank=True,null=True)
    candidate_name = models.CharField(max_length = 60)
    candidate_email = models.CharField(max_length = 60,default="")
    # cadidate_id = models.AutoField(primary_key=True,default=0)
    candidate_age = models.IntegerField()

    def __str__(self):
	       return "%s" %(self.candidate_name)

class Job_application_details(models.Model):

    # company_name = models.CharField(max_length = 60)
    # job_location = models.CharField(max_length = 60)
    # application_id=models.AutoField(primary_key=True,default=0)

    job = models.ForeignKey(Job_details,on_delete= models.CASCADE,default=0)
    # job_position = models.CharField(max_length = 60)
    candidate = models.ForeignKey(Candidate_personal_details, on_delete= models.CASCADE,default=0)
    # job_name = models.CharField(max_length = 60,default="")
    company_name = models.CharField(max_length = 60,null=True, blank=True)
    date = models.DateField(_("Date"), default=datetime.date.today)
    score_answer_relevance = models.FloatField(null=True, blank=True)
    score_grammar_analysis = models.FloatField(null=True, blank=True)
    score_sentiment_analysis = models.FloatField(null=True, blank=True)

    def __str__(self):
        return "%s" %(self.candidate)

class Emotion_output(models.Model):
	file_name = models.CharField(max_length=200)
	emo_output = JSONField()
	def __str__(self):
		return "%s %s" %(self.file_name, self.emo_output)

class Sentiment_output(models.Model):
	file_name_sentiment = models.CharField(max_length = 200)
	sentiment_score = JSONField()
	def __str__(self):
		return "%s %s" %(self.file_name_sentiment, self.sentiment_score)

class Similarity_output(models.Model):
	file_name_similarity = models.CharField(max_length = 200)
	similarity_score = models.CharField(max_length = 200)
	def __str__(self):
		return "%s %s" %(self.file_name_similarity, self.similarity_score)
