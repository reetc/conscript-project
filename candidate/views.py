from django.shortcuts import render
from company.models import Company_details,Job_details
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .models import Candidate_personal_details
from .models import Job_application_details


from keras.preprocessing import image
#import matplotlib.pyplot as plt
from keras.models import model_from_json
import numpy as np
import os
import shutil
import boto3
import json
import cv2
import math
from keras import backend as K

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from nltk import tokenize
import warnings
import gensim

# Create your views here.
def canhomepage(request):
	companies = Company_details.objects.all()
	print(companies)
	return render(request,'candidate/index.html',{'companies':companies})

def sendComp(request,ide):
    if request.method == 'POST':
        jobs = Job_details.objects.filter(company_id=ide)
        print(jobs)
        return render(request,'candidate/jobs.html',{'jobs':jobs})
    else:
    	return render(request, 'candidate/jobs.html')

def questions(request):
    return render(request, 'candidate/first.html')

@csrf_exempt
def webcam(request):
   if request.is_ajax():
       if request.method == 'POST':
           # request_data = request.body
           # data = json.loads(request.body)
           # print(request_data)
           # data = json.loads(request.body.decode('utf-8'))
           # print(data)
           # print(data)
           filename = request.POST.get('senddata')
           text_from_speech = request.POST.get('text_from_speech')
           print(filename)
           print(text_from_speech, 'text_from_speech')
           filename_vid = filename+'.mp4'
           s3 = boto3.resource('s3')
           bucket_name = 'recorded-video-bucket'
           s3.meta.client.download_file(bucket_name, filename_vid, filename_vid)
           print('video downloaded')
           print(os.getcwd())


           ################## emotion detection #########################
           bucket_name = 'face-emotion-detection'
           # Playing video from file:
           cap = cv2.VideoCapture(filename_vid)
           try:
               if not os.path.exists('data'):
                   os.makedirs('data')
           except OSError:
               print ('Error: Creating directory of data')

           currentFrame = 0
           while(True):
               ret, frame = cap.read()
               if (currentFrame % 32) == 0:
                   name = './data/frame' + str(currentFrame) + '.jpg'
                   print ('Creating...' + name)
                   cv2.imwrite(name, frame)
               currentFrame += 1
               if not ret:
                   break

           # When everything done, release the capture
           cap.release()
           cv2.destroyAllWindows()



           json_file = open('model.json','r')
           loaded_model_json = json_file.read()
           json_file.close()
           model = model_from_json(loaded_model_json)
           model.load_weights('facial_expression_model_weights.h5')

           currdir = os.getcwd()
           images = os.listdir(currdir + "/data")

           emotions = []
           emo_dict = {'angry': 0, 'disgust': 0, 'fear': 0, 'happy': 0, 'sad': 0, 'surprise': 0, 'neutral': 0}
           for frame in images:
               try:
                   img = image.load_img(currdir+"/data/"+ frame, color_mode = 'grayscale', target_size=(48, 48))
               except:
                   print(1)

               x = image.img_to_array(img)
               x = np.expand_dims(x, axis = 0)

               x /= 255

               custom = model.predict(x)
               print()
               emo = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']
               A = custom[0]
               npindex = list(np.where(A==A.max()))
               index = npindex[0][0]
               print(emo[index], frame)
               emotions.append(emo[index])
               emo_dict[emo[index]] += 1
               with open('outfile.json', 'w') as fp:
                   json.dump(emo_dict, fp)
               # emotion_analysis(custom[0])
               filename = 'outfile.json'
               s3.meta.client.upload_file(filename, bucket_name, filename)
           print()
           print(emo_dict)
           shutil.rmtree('data')
           os.remove('outfile.json')
           os.remove(filename_vid)
           K.clear_session()

           ################## sentiment analysis #########################
           bucket_name = 'texts-converted-from-speech-01'
           with open('text_from_speech.txt', 'w') as f:
               f.write(text_from_speech)
           s3.meta.client.upload_file('text_from_speech.txt', bucket_name, 'text_from_speech.txt')
           # os.remove('text_from_speech.txt')
           print('text converted from speech uploeaded to AWS')


           bucket_name = 'sentiment-analysis-for-text'
           sid = SentimentIntensityAnalyzer()
           scores = sid.polarity_scores(text_from_speech)
           print()
           print("The sentiment analysis is:")
           print()
           with open('sentiment.txt', "w") as f:
               for key in sorted(scores):
                   print('{0}: {1}, '.format(key, scores[key]), end='')
                   f.write('\n')
                   f.write('{0}: {1},'.format(key, scores[key]))
                   f.write('\n')
           s3.meta.client.upload_file('sentiment.txt', bucket_name, 'sentiment.txt')
           print()
           print('Sentiment analysis done and file uploeaded to AWS')
           print()
           os.remove('sentiment.txt')

           ################## Answer Relevance #########################
           bucket_name = 'answer-relavance'

           warnings.filterwarnings("ignore", category=DeprecationWarning)

           file1 = open("modelanswer.txt","r")
           p=file1.read()
           print("****************Model Answer******************")
           print(p)
           raw_documents=tokenize.sent_tokenize(p)
           from nltk.tokenize import word_tokenize
           gen_docs = [[w.lower() for w in word_tokenize(text)]
                       for text in raw_documents]

           dictionary = gensim.corpora.Dictionary(gen_docs)
           corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
           tf_idf = gensim.models.TfidfModel(corpus)
           s = 0
           for i in corpus:
               s += len(i)

           sims = gensim.similarities.Similarity(currdir+'/answer_relavance',tf_idf[corpus], num_features=len(dictionary))

           file2 = open("text_from_speech.txt","r")
           p2=file2.read()
           print("****************  Given Answer   ******************")
           print(p2)

           query_doc = [w.lower() for w in word_tokenize(p2)]
           query_doc_bow = dictionary.doc2bow(query_doc)
           query_doc_tf_idf = tf_idf[query_doc_bow]
           array=sims[query_doc_tf_idf]
           sum=0.0

           for i in array:
               print(i)
               sum=sum+i

           print("Final Similarity Index: ",(sum/(len(raw_documents))))

           answer = str(sum/len(raw_documents))
           with open('similarity.txt', "w") as similarity:
               similarity.write(answer)
           s3.meta.client.upload_file('similarity.txt', bucket_name, 'similarity.txt')

           similarity.close()
           file1.close()
           file2.close()

           os.remove('text_from_speech.txt')
           os.remove('similarity.txt')
           print('All are successfull')
       return render(request, 'candidate/webcam.html')
   else:
       return render(request, 'candidate/webcam.html')



def register(request):
	if request.method == 'POST':
		username = request.POST.get('email')
		password = request.POST.get('password')
		name = request.POST.get('name')
		user = User.objects.create(first_name = name,username = username,)
		user.set_password(password)
		user.save()
		candidate = Candidate_personal_details()
		candidate.user=User.objects.get(username=request.POST['email'])
		candidate.candidate_name=request.POST['name']
		candidate.candidate_email=request.POST['email']
		candidate.candidate_age=request.POST['age']
		candidate.save()
		user = authenticate(username = username, password = password)
		login(request, user)
		return redirect('/candidate/canhomepage/')
	else:
		return render(request,'candidate/register.html')





def login_blog(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user :
            if user.is_active:
                login(request,user)
                return redirect('/candidate/canhomepage/')
            else:
                return HttpResponse('Disabled Account')
        else:
            return HttpResponse("Invalid Login details.Are you trying to Sign up?")
    else:
        return render(request,'candidate/login.html')

def logout_blog(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request,'candidate/logout.html')
    else:
        return HttpResponseRedirect('/login/')
