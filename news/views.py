from django.shortcuts import render
from django.views.generic import ListView
from .models import Category, Region, News

def home(request):
    latest_new = News.objects.filter().order_by('-id')[0:1]
    other_news = News.objects.filter().order_by('-id')[1:12]
    categories = Category.objects.all()
    regions = Region.objects.all()

    context = {
        'latest_new': latest_new,
        'other_news': other_news,
        'categories': categories,
        'regions': regions
    }

    return render(request, 'home.html', context)

def detail(request):
    news = News.objects.get(id=id)
    category = Category.objects.get(id=news.category.id)
    rel_news = News.objects.filter(category=category).exclude(id=id)

    context = {
        'news': news,
        'category': category,
        'rel_news': rel_news
    }

    return render(request, 'detail.html', context)

class AllViews(ListView):
    model = News
    template_name = 'all-news.html'

def category_detail(request):
    category = Category.objects.get(id=id)
    news = News.objects.filter(category=category)

    return render(request, 'category-news.html',{
        'category': category,
        'news': news
    })

def region_detail(request):
    region = Region.objects.get(id=id)
    news = News.objects.filter(region=region)

    return render(request, 'region-news.html',{
        'region': region,
        'news': news
    })

