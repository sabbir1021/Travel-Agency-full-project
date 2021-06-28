from django.shortcuts import render , get_object_or_404 , redirect
from .models import Country , Articale , Client , Blog , BlogComment , Subscribe , BlogCategory , ArticaleContact , Contact , Review
from django.db.models import Max, Min , Count , Sum
from .forms import RegisterUser, CommentForm , SubscribeForm  , feedbackForm , BlogForm , ArticaleContactForm , ContactForm , ReviewForm
from django.core.paginator import Paginator
from django.contrib import messages
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from tour.settings import EMAIL_HOST_USER
from . import forms


# Create your views here.

def index(request):
    post = Articale.objects.all().order_by("-id")[0:6]
    ppost = Country.objects.all()
    count = Articale.objects.filter(country__id=2).aggregate(Count('country'))['country__count']
    cpost = Client.objects.all().order_by("-id")[0:4]
    blogpost = Blog.objects.all().filter(categorys__id=1).order_by("-id")[0:3]
    sform = SubscribeForm(request.POST or None)
    check = str(sform['email'].value())
    sub = Subscribe.objects.all().filter(email=check)
    if sform.is_valid():
        if sub:
            messages.warning(request, 'you are already subscribe')
        else:
            instance=sform.save(commit=False)
            instance.save();
            messages.success(request, 'Subscribe is Successfuly done')
    #country = Articale.objects.all().filter(country=id.ppost)
    if 'place' in request.GET:
        fil_1 = request.GET.get('place')
        fil_2 = request.GET.get('date')
        if fil_1 == "Where to go?":
            fil_1 = ''

        if fil_1 == '' and fil_2 == '':
            sar = Articale.objects.all()
            return render(request, "index.html" , {"post":sar} )
        if fil_2 == '':
            sar = Articale.objects.all().filter(name=fil_1)
            return render(request, "index.html" , {"post":sar} )
        if fil_1=='':
            sar = Articale.objects.all().filter(date=fil_2)
            return render(request, "index.html" , {"post":sar} )
        if fil_1 and fil_2:
            sar = Articale.objects.all().filter(name=fil_1 , date=fil_2)
            return render(request, "index.html" , {"post":sar} )
    return render(request , "index.html" , {"post":post , 
    "ppost":ppost , 
    "country":country , 
    "count":count, 
    "cpost":cpost,
    "blogpost":blogpost,
    "sform":sform})

def country(request, id):
    post = Articale.objects.all().filter(country=id)
    cate = get_object_or_404(Country, pk=id)
    return render(request, "country.html" , {"post":post , "cate":cate})

def about(request):
    blogpost = Blog.objects.all().filter(categorys__id=1).order_by("-id")[0:3]
    cpost = Client.objects.all().order_by("-id")[0:4]
    return render(request , "about.html" ,{"blogpost":blogpost, "cpost":cpost })


def destination(request):
    post = Articale.objects.all()
    paginator = Paginator(post, 6)  # Show 25 contacts per page
    page_number = request.GET.get('page')
    pagpost = paginator.get_page(page_number)
    blogpost = Blog.objects.all().filter(categorys__id=1).order_by("-id")[0:3]
    sform = SubscribeForm(request.POST or None)
    check = str(sform['email'].value())
    sub = Subscribe.objects.all().filter(email=check)
    if sform.is_valid():
        if sub:
            messages.warning(request, 'you are already subscribe')
        else:
            instance=sform.save(commit=False)
            instance.post=post
            instance.save();
            messages.success(request, 'Subscribe is Successfuly done')
    if 'min_price' in request.GET:
        filter_price1 = request.GET.get('min_price')
        filter_price2 = request.GET.get('max_price')
        if filter_price1 =='':
            filter_price1=0
        if filter_price2=='':
            filter_price2 = Articale.objects.aggregate(Max('price'))['price__max']
        my_products = Articale.objects.filter(price__range=(filter_price1,filter_price2))
        return render(request, "travel_destination.html" , {"post":my_products} )
    if 'place' in request.GET:
        fil_1 = request.GET.get('place')
        fil_2 = request.GET.get('date')
        if fil_1 == "Where to go?":
            fil_1 = ''

        if fil_1 == '' and fil_2 == '':
            sar = Articale.objects.all()
            return render(request, "travel_destination.html" , {"post":sar} )
        if fil_2 == '':
            sar = Articale.objects.all().filter(name=fil_1)
            return render(request, "travel_destination.html" , {"post":sar} )
        if fil_1=='':
            sar = Articale.objects.all().filter(date=fil_2)
            return render(request, "travel_destination.html" , {"post":sar} )
        if fil_1 and fil_2:
            sar = Articale.objects.all().filter(name=fil_1 , date=fil_2)
            return render(request, "travel_destination.html" , {"post":sar} )
        
    return render(request, "travel_destination.html", {"post":pagpost , 
    "blogpost":blogpost , 
    "sform" : sform
     } )

def blog(request):
    post = Blog.objects.all()
    paginator = Paginator(post, 3)  # Show 25 contacts per page
    page_number = request.GET.get('page')
    pagpost = paginator.get_page(page_number)
    ppost = BlogCategory.objects.all()
    recentart = Articale.objects.all()[0:4]
    sform = SubscribeForm(request.POST or None)
    check = str(sform['email'].value())
    sub = Subscribe.objects.all().filter(email=check)
    if sform.is_valid():
        if sub:
            messages.warning(request, 'you are already subscribe')
        else:
            instance=sform.save(commit=False)
            instance.save();
            messages.success(request, 'Subscribe is Successfuly done')
    return render(request , "blog.html" , {"post":pagpost , "recentart":recentart , "sform":sform,"ppost":ppost})

def blogcategory(request , id):
    post = Blog.objects.all().filter(categorys=id)
    paginator = Paginator(post, 3)  # Show 25 contacts per page
    page_number = request.GET.get('page')
    pagpost = paginator.get_page(page_number)
    cate = get_object_or_404(BlogCategory, pk=id)
    ppost = BlogCategory.objects.all()
    recentart = Articale.objects.all()[0:4]
    sform = SubscribeForm(request.POST or None)
    check = str(sform['email'].value())
    sub = Subscribe.objects.all().filter(email=check)
    if sform.is_valid():
        if sub:
            messages.warning(request, 'you are already subscribe')
        else:
            instance=sform.save(commit=False)
            instance.post=post
            instance.save();
            messages.success(request, 'Subscribe is Successfuly done')
    return render(request , "blogcategory.html" , {"post":pagpost , "recentart":recentart , "sform":sform,"ppost":ppost,"cate":cate})


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.post=post
        instance.save();
        messages.success(request, 'Contact message Successfuly done')
    if request.method == 'POST':
        sub = ContactForm(request.POST or None)
        subject = str(sub['subject'].value())
        message = str(sub['message'].value())
        recepient = str(sub['email'].value())
        send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'contact.html', {'recepient': recepient})
    return render(request , "contact.html" , {'form':form})

def single(request , id):
    post = get_object_or_404(Articale , id=id)
    recent = Articale.objects.all().exclude(id=id)[0:3]
    form = ArticaleContactForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.post=post
        instance.save();
        messages.success(request, 'Contact message Successfuly done')
    sform = SubscribeForm(request.POST or None)
    check = str(sform['email'].value())
    sub = Subscribe.objects.all().filter(email=check)
    if sform.is_valid():
        if sub:
            messages.warning(request, 'you are already subscribe')
        else:
            instance=sform.save(commit=False)
            instance.post=post
            instance.save();
            messages.success(request, 'Subscribe is Successfuly done')
    return render(request , "single.html" , {"post":post,"recent":recent, "sform":sform , "form":form})

def review(request , id):
    post = get_object_or_404(Articale , id=id)
    recent = Articale.objects.all().exclude(id=id)[0:3]
    com = Review.objects.filter(post=id)
    count = Review.objects.filter(post=id).aggregate(Count('mark'))['mark__count']
    reviewsum = Review.objects.filter(post=id).aggregate(Sum('mark'))['mark__sum']
    if True:    
        if count:
            result = reviewsum / count 
        else:
            result = 0
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.post=post
        instance.save();
        messages.success(request, 'Your Review Successfuly done')
    sform = SubscribeForm(request.POST or None)
    check = str(sform['email'].value())
    sub = Subscribe.objects.all().filter(email=check)
    if sform.is_valid():
        if sub:
            messages.warning(request, 'you are already subscribe')
        else:
            instance=sform.save(commit=False)
            instance.post=post
            instance.save();
            messages.success(request, 'Subscribe is Successfuly done')
    return render(request , "review.html" , {"post":post,"recent":recent, "sform":sform , "form":form , "com":com , "result":result})


def blogsingle(request , id):
    post = get_object_or_404(Blog , id=id)
    ppost = BlogCategory.objects.all()
    recentart = Articale.objects.all().exclude(id=id)[0:5]
    recent = Blog.objects.all().exclude(id=id)[0:4]
    first = Blog.objects.first()
    last = Blog.objects.last()
    if True:
        if post.id > 1:
            a=id-1
            while(True):
                if Blog.objects.filter(id=a):
                    firstpost = get_object_or_404(Blog, pk=a)
                    break
                else:
                    a= a-1
        else:
            firstpost = get_object_or_404(Blog, pk=id)
    if True:
        if post.id < last.id:
            a=id+1
            while(True):
                if Blog.objects.filter(id=a):
                    lastpost = get_object_or_404(Blog, pk=a)
                    break
                else:
                    a= a+1
        else:
            lastpost = get_object_or_404(Blog, pk=id)

    sform = SubscribeForm(request.POST or None)
    check = str(sform['email'].value())
    sub = Subscribe.objects.all().filter(email=check)
    if sform.is_valid():
        if sub:
            messages.warning(request, 'you are already subscribe')
        else:
            instance=sform.save(commit=False)
            instance.post=post
            instance.save();
            messages.success(request, 'Subscribe is Successfuly done')
    com = BlogComment.objects.filter(post=id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.post=post
        instance.save();
        messages.success(request, 'Comment is Successfylly done')
    return render(request , "blogsingle.html" , {
        "post":post,
        "recent":recent , 
        "recentart":recentart , 
        "com":com , 
        "form":form,
        "first":first,
        "last":last,
        "firstpost":firstpost,
        "lastpost":lastpost,
        "ppost":ppost,
        "sform":sform
        })


def register(request):
    form = RegisterUser(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save();
        messages.success(request, 'Register is Successfully Completed')
        return redirect('login')
    return render(request, "register.html" , {"form":form})

def feedback(request):
    if request.user.is_authenticated:
        form = feedbackForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save();
            messages.success(request, 'thank you for your openion')
            return redirect('index')
    else:
        return redirect('login')
    return render(request, "feedback.html" , {"form":form})

def post(request):
    if request.user.is_authenticated:
        post = BlogCategory.objects.all()
        form = BlogForm(request.POST or None , request.FILES or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save();
            messages.success(request, 'thank you for your openion')
            return redirect('index')
    else:
        return redirect('login')
    return render(request, "post.html" , {"form":form , "post":post})

