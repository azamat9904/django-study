from django.shortcuts import render
from django.http import HttpResponse
from .models import News
from django.shortcuts import render
# Create your views here.

def index(request):
    news = News.objects.all()
    context = {
        "news": news,
        "title": "Список новостей"
    }
    return render(request, template_name='news/index.html', context=context)
