from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import Question
from django.template import loader

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def index1(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index1.html')
    context = {
        'latest_question_list':latest_question_list
    }
    return HttpResponse(template.render(context,request))

def index2(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list':latest_question_list
    }
    return HttpResponse(render(request,'polls/index2.html',context))



def detail(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/details.html',{'question':question})

def results(request,question_id):
    response = "You're looking at the results %s"
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("You're voting on question %s." % question_id)

