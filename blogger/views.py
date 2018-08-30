from django.shortcuts import render,HttpResponse
from blogger.models import blogpost,comments

# Create your views here.

def home(request):
	post=blogpost.objects.all()
	return render (request,"home.html",{"post":post})
	# return render(request,"home.html",{"post":"vivek"})

def comment(request,post_id):
	mypost=blogpost.objects.get(pk=post_id)
	com=comments.objects.filter(post=mypost)
	context={"mypost":mypost,"com":com}
	return render(request,"post.html",context)

