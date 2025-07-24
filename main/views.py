from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from blogs.models import Blog, BlogStats
from collections import defaultdict

def landingPage(request):
    return render(request,'pages/index.html')

def aboutPage(request):
    return render(request, 'pages/aboutus/about_page.html')

def loginPage(request):
    return render (request, 'pages/auth/login.html')

def signupPage(request):
    return render(request, 'pages/auth/signup.html')

def blogPage(request):
    blogs  =  Blog.objects.filter(status='Active').order_by('-created_at')
    return render(request, 'pages/blogs/blogs.html', {'blogs':blogs})

@login_required(login_url='/auth/log-in/')
def profilePage(request):
    return render(request, 'pages/auth/profile.html')

@login_required(login_url='/auth/log-in/')
def dashboard(request):
    user_blogs = Blog.objects.filter(author=request.user)
    blogstats = BlogStats.objects.filter(blog__in=user_blogs).order_by('created_at')

    click_data = defaultdict(int)
    unique_data = defaultdict(int)

    for b in blogstats:
        date_str = b.created_at.strftime('%Y-%m-%d')
        click_data[date_str] += b.blog_clicks
        unique_data[date_str] += b.unique_views

    click_date = list(click_data.keys())  # Assumes both click_data and unique_data have same dates
    blogclicks = [click_data[date] for date in click_date]
    unique_views = [unique_data[date] for date in click_date]

    return render(request, 'pages/dashboard/writer/dashboard.html', {
        "click_date": click_date,
        "blogclicks": blogclicks,
        "unique_views": unique_views
    })
    
def blogList(request):
    blogs = Blog.objects.filter( author = request.user).order_by('-created_at')
    return render(request, 'pages/dashboard/writer/blogList.html', {'blogs':blogs})

@login_required(login_url="/auth/log-in")
def adminDashboard(request):
    if request.user.profile.role=="Admin":
        return render(request, 'pages/dashboard/admin/dashboard.html')
    else:
        return redirect('/writer/dashboard')

