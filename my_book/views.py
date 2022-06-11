#from pydoc_data.topics import 
from django.shortcuts import render, redirect 
from .models import Topic,Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required 

# Create your views here.
def home(request):
    '''render the home page to the user'''
    my_topics=Topic.objects.all()
    return render (request,'index.html',{'topic':my_topics})

@login_required
def content(request,topic_id):
    '''render the home page to the user'''
    topic = Topic.objects.get(id=topic_id)
    if request.method == 'POST':
        comment =Comment()
        comment.topic = topic
        comment.owner = request.user
        comment.body = request.POST.get('user_comment')
        comment.save()
    comments = topic.comment_set.all()
    return render (request,'content.html',{'topic':topic,'comments':comments})

def signup(request):
    '''render the sign-up page to the user'''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    else:
        form = UserCreationForm()
    return render (request,'signup.html',{'form':form})


#def log(request):
   # '''render the log in page to the user'''
    #return render (request,'log.html')


def profile(request):
    '''render the profile page to the user'''
    return render (request,'profile.html')

def edit(request):
    '''render the edit page to the user'''
    return render (request,'edit.html')

def email(request):
    '''render the edit page to the user'''
    return render (request,'email.html')