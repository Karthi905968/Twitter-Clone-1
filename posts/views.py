from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from .forms import PostForm

def index(request):
    # If the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # if the form is valid
        if form.is_valid():
            #Yes, Svae
            form.save()
            #Redirect to Home
            return HttpResponseRedirect('/')
    
        else:
            #No, Show Error
            return HttpResponseRedirect(form.errors.as_json())

    # Get all posts, limit = 20
    posts = Post.objects.all()[:20]
    

    # Show 
    return render(request, 'posts.html',
                 {'posts':posts} )


def delete(request, post_id):
    #Frist Post 
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')

def edit(request, post_id):
    post = Post.objects.get(id = post_id)
    if request.method == 'GET':
        posts = Post.objects.get(id = post_id)
        return render(request, 'edit.html', {'posts': posts})
    if request.method == 'POST':
        posts = Post.objects.get(id = post_id)
        form = PostForm(request.POST, request.FILES, instance = posts)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('not valid')

def likes(request, post_id):
    like = Post.objects.get(id = post_id)
    if like.likes == 0:
        like.likes = 1
        like.save()
        return HttpResponseRedirect('/')
    else:
        like.likes = 0
        like.save()
        return HttpResponseRedirect('/')
        

        

