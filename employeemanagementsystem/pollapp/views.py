from django.shortcuts import render
from django.http import Http404,HttpResponse
from pollapp.models import *


# Create your views here.
def index(request):
    context={}
    questions=Question.objects.all()
    context['title']='polls'
    context['questions']= questions
    return render(request,'pollapp/index.html',context)

def detail(request,id=None):
    context={}
    try:
        question=Question.objects.get(id=id)
    except:
        raise Http404
    context['question']=question
    return render(request,'pollapp/details.html',context)


def poll(request,id=None):
    if request.method=="GET":
        try:
            question = Question.objects.get(id=id)
        except:
            raise Http404
        context={}
        context['question'] = question
        return render(request, 'pollapp/poll.html', context)
    if request.method=="POST":
            user_id=1
            print(request.POST)
            data=request.POST
            ret=Answer.objects.create(user_id=user_id,choice_id=data['choice'])
            if ret:
                return HttpResponse("your vote is saved successfully")
            else:
                return HttpResponse("your vote is not saved ")


