from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Category, Region, News

def home(request):
    all_news = News.objects.filter(is_published=True).order_by('-created_at')
    latest_new = all_news.first()
    other_news = all_news[1:13]
    categories = Category.objects.all()
    regions = Region.objects.all()

    context = {
        'latest_new': latest_new,
        'other_news': other_news,
        'categories': categories,
        'regions': regions
    }

    return render(request, 'home.html', context)

def detail(request, id):
    news = get_object_or_404(News, id=id, is_published=True)
    news.view_count += 1
    news.save()
    category = news.category
    rel_news = News.objects.filter(category=category, is_published=True).exclude(id=id)[:5]

    context = {
        'news': news,
        'category': category,
        'rel_news': rel_news
    }

    return render(request, 'detail.html', context)

class AllViews(ListView):
    model = News
    template_name = 'all-news.html'
    context_object_name = 'news_list'
    paginate_by = 12

    def get_queryset(self):
        return News.objects.filter(is_published=True).order_by('-created_at')

def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    news = News.objects.filter(category=category, is_published=True).order_by('-created_at')

    return render(request, 'category-news.html', {
        'category': category,
        'news': news
    })

def region_detail(request, id):
    region = get_object_or_404(Region, id=id)
    news = News.objects.filter(region=region, is_published=True).order_by('-created_at')

    return render(request, 'region-news.html', {
        'region': region,
        'news': news
    })