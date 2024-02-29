from django.shortcuts import render, redirect
from django.contrib.staticfiles import finders 
from .models import SocialMediaPost
from .models import SocialMediaPost
from .forms import SocialMediaPostForm
import json

def analytics(request):
    mock_data_path = finders.find('mock_data.json')  # Get the path to mock_data.json
    with open(mock_data_path) as json_file:
        data = json.load(json_file)
    return render(request, 'analytics.html', {
        'total_likes': data['likes'],
        'total_shares': data['shares'],
        'total_comments': data['comments']
    })

def manage_posts(request):
    posts = SocialMediaPost.objects.all()
    return render(request, 'manage_posts.html', {'posts': posts})


def create_post(request):
    if request.method == 'POST':
        form = SocialMediaPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_posts')
    else:
        form = SocialMediaPostForm()
    return render(request, 'create_post.html', {'form': form})

def edit_post(request, pk):
    post = SocialMediaPost.objects.get(pk=pk)
    if request.method == 'POST':
        form = SocialMediaPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('manage_posts')
    else:
        form = SocialMediaPostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})

def delete_post(request, pk):
    post = SocialMediaPost.objects.get(pk=pk)
    post.delete()
    return redirect('manage_posts')


def home(request):
    return render(request, 'home.html')
