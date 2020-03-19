from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm 
from blog.models import Post
from users.serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')



def post_list(request):
    post=Post.objects.all()
    serializer = PostSerializer(post, many=True)
    return Response(serializer.data) 

