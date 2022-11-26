
from http.client import HTTPResponse
from multiprocessing import context
from typing import Generic
from unicodedata import category
from urllib import response
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render
from django.utils import timezone
from .models import Post, User, CategoryTable, Tags, Comment
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, SignupForm, LoginForm, CommentForm,EditProfileForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as wahidlogin
from django.contrib import messages
from . import forms
from django.http import HttpResponseRedirect
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

#profile page using user name as url
@login_required
def profile_page(request):
    user = get_object_or_404(User, id=request.user.id)
    return render(request, 'blog/profile.html', {'user': user})

@login_required
def edit_profile(request):
    form = forms.EditProfileForm()
    if request.method == 'POST':
        form = EditProfileForm(request.POST,instance=request.user)
        if form.is_valid:
            form.save()
            return redirect('post_list')    
    return render(request, 'blog/editprofile.html',{'form': form})

def post_list(request):
    posts = Post.objects.all().order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
	post = get_object_or_404(Post, slug=slug)
	comments = post.comments.filter(parent__isnull=True)
	comment_form= CommentForm()
	if request.method == 'POST':
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			try:
				parent_id = int(request.POST.get('parent_id'))
			except:
				parent_id = None
			if parent_id:
				parent_obj = Comment.objects.get(id=parent_id)
				if parent_obj:
					replay_comment = comment_form.save(commit=False)
					replay_comment.parent = parent_obj
			new_comment = comment_form.save(commit=False)
			new_comment.post = post
			new_comment.save()
			return redirect('post_detail', slug=post.slug)
		else:
			comment_form = CommentForm()
	return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments,'comment_form': comment_form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

# This is for user registration.
def register(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        print(form.is_valid(), form.errors)
        if form.is_valid():
            print("hdghfkj")
            user_obj = form.save()
            user = User.objects.filter(
                     username=form.cleaned_data["username"]).last()
            wahidlogin(request, user)
            messages.success(request, "Registration successful.")
            return redirect('post_list')
    else:
        form = SignupForm()
    return render(request, 'blog/register.html', {'form': form, })

# Views for login
def login(request):
    form = forms.LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get("password")
            user = User.objects.filter(username=username).last()
            if user:
                user = authenticate(username=username, password=password)
                wahidlogin(request, user)
                return redirect("post_list")
            else:
                messages.error(request, "Invalid username or password")
        else:
            form = forms.LoginForm()
    return render(request, "blog/login.html", context={"form": form, })

# for logout user.....
def logout_user(request):
    logout(request)
    return redirect('login')

# For Category of post list...
def category_list(request, slug):
    post = get_object_or_404(Post, slug=slug)
    category = post.category

    posts = Post.objects.filter(category=category)
    context = {
        'category': category,
        'posts': posts
    }
    print(category)
    return render(request, 'blog/category_list.html', context)

def tags_list(request, slug):
    tag= Tags.objects.filter(slug=slug).last()
    posts =Post.objects.filter(tag = tag).all()
    context = {
        'posts' : posts
    }
    return render(request,'blog/tags_list.html',context)

