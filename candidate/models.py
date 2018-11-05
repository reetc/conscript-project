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

    def __str__(self):
	       return "%s" %(self.candidate_name)

class Job_application_details(models.Model):

    # company_name = models.CharField(max_length = 60)
    # job_location = models.CharField(max_length = 60)
    # application_id=models.AutoField(primary_key=True,default=0)

# <<<<<<< HEAD
#     job = models.ForeignKey(Job_details,on_delete= models.CASCADE,default=0)
# =======
    job_id=models.ForeignKey(Job_details,on_delete= models.CASCADE,default=0)
# >>>>>>> abd0f378cdc866ac75badbcfad0054ff3ab8bdcd
    # job_position = models.CharField(max_length = 60)
    candidate = models.ForeignKey(Candidate_personal_details, on_delete= models.CASCADE,default=0)
    # job_name = models.CharField(max_length = 60,default="")
    company_name = models.CharField(max_length = 60,null=True, blank=True)
    date = models.DateField(_("Date"), default=datetime.date.today)
    score_answer_relevance = models.FloatField(null=True, blank=True)
    score_grammar_analysis = models.FloatField(null=True, blank=True)
    score_sentiment_analysis = models.FloatField(null=True, blank=True)
# <<<<<<< HEAD


    def __str__(self):
        return "%s" %(self.candidate)
# # additional scores if any
# =======
    
#     # additional scores if any
# >>>>>>> abd0f378cdc866ac75badbcfad0054ff3ab8bdcd
