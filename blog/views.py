from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .form import BlogPost #form.py 의 BlogPost import

def home(request):
    blogs = Blog.objects
    #모든 블로그 글을 대상으로
    blog_list = Blog.objects.all()
    #블로그 객체 3개를 한 페이지로 묶기 
    paginator = Paginator(blog_list, 3)
    #request된 페이지가 뭔지 알아내고 (request페이지를 변수에 담고)
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogs' : blogs, 'posts' : posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog' : blog_detail})

def new(request): 
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))

def blogpost(request):
    # 1. 입력된 내용을 처리하는 기능 => POST
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid(): #form 입력 검사
            post = form.save(commit=False) #아직 저장 x, 모델 객체만 반환 pub_date 채워줘야 함
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    # 2. 빈 페이지를 띄어주는 기능  => GET
    #new.html에 빈 페이지 띄우기
    else: 
        form = BlogPost()
        return render(request, 'new.html', {'form':form}) 