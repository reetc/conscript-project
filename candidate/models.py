from django.db import models
from company.models import Job_details
from django.utils.translation import gettext as _
import datetime

# Create your models here.
class Candidate_personal_details(models.Model):
    candidate_name = models.CharField(max_length = 60)
    candidate_email = models.CharField(max_length = 60,default="")
    # cadidate_id = models.AutoField(primary_key=True,default=0)
    candidate_age = models.IntegerField()

class Job_application_details(models.Model):

    # company_name = models.CharField(max_length = 60)
    # job_location = models.CharField(max_length = 60)
    # application_id=models.AutoField(primary_key=True,default=0)

    job_id=models.ForeignKey(Job_details,on_delete= models.CASCADE,default=0)
    # job_position = models.CharField(max_length = 60)
    candidate_id_Foreign= models.ForeignKey(Candidate_personal_details, on_delete= models.CASCADE,default=0)
    date = models.DateField(_("Date"), default=datetime.date.today)
    score_answer_relevance = models.FloatField(null=True, blank=True)
    score_grammar_analysis = models.FloatField(null=True, blank=True)
    score_sentiment_analysis = models.FloatField(null=True, blank=True)
    
    # additional scores if any
