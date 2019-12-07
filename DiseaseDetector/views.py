# from django.shortcuts import render
# from django.contrib.auth import authenticate, login, logout
# from DiseaseDetector.forms import UserLoginForm

from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from django.http import HttpResponse
from django.http import JsonResponse
from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
import json

from DiseaseDetector.forms import UserLoginForm, UserRegistrationForm
from DiseaseDetector.models import *
from .domain.survey import surveyjs_io_json, OncologyAlertnessQuestionnaire
from .ML.predict_diagnosis import *
from .ML.train_ml_model import *


def main(request):
    return redirect('signin')

def signup(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST, request.FILES)
		if form.is_valid():
			user = form.save()
			user.set_password(form.cleaned_data['password'])
			user.save()
			login(request, user)
			return redirect('/')
	else:
		form = UserRegistrationForm()
		logout(request)
	return render(request, 'DiseaseDetector/signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/survey')

    if request.method == 'GET':
        if auth.get_user(request).is_anonymous:
            form = UserLoginForm()
            return render(request, 'DiseaseDetector/signin.html', {'form': form})
        else:
            return redirect('/survey')
    


def signout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')


def profile(request, username):
    user = User.objects.by_username(username)
    if user is not None:
        return render(request, 'DiseaseDetector/profile.html', {'profile': user})
    else:
        raise Http404


def survey(request):
    #if auth.get_user(request).is_anonymous:
    #    return redirect('/signin')
    #else:
        return render(request, 'DiseaseDetector/survey.html', )

def survey_questionnaire(request: HttpRequest) -> HttpResponse:
    return JsonResponse(surveyjs_io_json, safe=False)

@csrf_exempt
def survey_response(request):
    result = OncologyAlertnessQuestionnaire.from_json(request.body)
    result_as_json = result.to_json()
    result_as_dict = json.loads(result_as_json)
    print(result_as_dict)
    # TODO: create database for answer
    # TODO: save as json to database V

    question = Question.objects.create(Doctor="", Datetime=20191212173212, FIO="", Acception=True, 
                                        q0=result_as_dict['q0'], q1=result_as_dict['q1'], q2=result_as_dict['q2'],
                                        q3=result_as_dict['q3'], q4=result_as_dict['q4'], q5=result_as_dict['q5'],
                                        q6=result_as_dict['q6'], q7=result_as_dict['q7'], q8=result_as_dict['q8'],
                                        q9=result_as_dict['q9'], q10=result_as_dict['q10'], q11=result_as_dict['q11'],
                                        q12=result_as_dict['q12'], q13=result_as_dict['q13'],q14=result_as_dict['q14'], 
                                        q15=result_as_dict['q15'], q16=result_as_dict['q16'],q17=result_as_dict['q17'], 
                                        q18=result_as_dict['q18'], q19=result_as_dict['q19'],q20=result_as_dict['q20'], 
                                        q21=result_as_dict['q21'], q22=result_as_dict['q22'],q23=result_as_dict['q23'], 
                                        q24=result_as_dict['q24'], q25=result_as_dict['q25'],q26=result_as_dict['q26'], 
                                        q27=result_as_dict['q27'], q28=result_as_dict['q28'],q29=result_as_dict['q29'], 
                                        q30=result_as_dict['q31'], q31=result_as_dict['q31'],q32=result_as_dict['q32'])
    question.save()

    print(int(predict_diagnosis(json_to_arr(result_as_json))))