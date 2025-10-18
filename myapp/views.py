from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post

def home(request):

    posts = post.objects.all().order_by('created_at')
    return render(request, 'myapp/home.html', {'posts': posts})   # the {'posts': posts})  is passed as dictionary to the template


def post_create(request) :
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        if title and content:
            post.objects.create(title = title , content = content) #this is a form handling

            return redirect('home')
    return render (request, 'posts/post_form.html', {'form_type ': 'create'})

def post_details(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request,'post/post_detail.html', {'post': post})


def post_edit(request,pk):
    post = get_object_or_404(post,pk=pk)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()

        return redirect ('post_detail', pk=post.pk)
    return render (request, 'posts/post_form.html',{'posts': post, 'form_type': 'Edit'})



def post_delete (request, pk):
    post = get_object_or_404 (Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect ('home')
    return render (request, 'posts/post_confirm_delete.html', {'post': post})