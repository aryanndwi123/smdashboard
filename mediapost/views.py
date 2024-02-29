from django.shortcuts import render, redirect
from .models import SocialMediaPost
from .models import SocialMediaPost
from .forms import SocialMediaPostForm
import json
from django.contrib.staticfiles import finders
from django.http import HttpResponseServerError

def analytics(request):
    # Attempt to find the path to mock_data.json
    mock_data_path = finders.find('mock_data.json')
    
    # Check if mock_data_path is None
    if not mock_data_path:
        return HttpResponseServerError("Mock data file not found.")

    try:
        # Attempt to open and read the JSON file
        with open(mock_data_path) as json_file:
            data = json.load(json_file)
    except Exception as e:
        return HttpResponseServerError("Error loading mock data: {}".format(str(e)))

    # Extract data and pass it to the template
    return render(request, 'analytics.html', {
        'total_likes': data.get('likes', 0),  # Default to 0 if key not found
        'total_shares': data.get('shares', 0),  # Default to 0 if key not found
        'total_comments': data.get('comments', 0)  # Default to 0 if key not found
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
