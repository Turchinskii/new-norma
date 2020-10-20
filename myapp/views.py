import locale

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views import View
from myapp.models import News


class NewsListView(View):
    def get(self, request):
        locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
        news_list = News.objects.all().order_by('-date')
        news_dir = {}
        for news in news_list:
            if news.date.strftime("%d %B, %A") in news_dir:
                news_dir[news.date.strftime("%d %B, %A")].append(news)
            else:
                news_dir.update({news.date.strftime("%d %B, %A"): [news]})
        return render(request, 'myapp/news-list.html', {'news_dir': news_dir})


class NewsInfoView(View):
    def get(self, request, **news_id):
        news = get_object_or_404(News, id=news_id['pk'])
        news_list = News.objects.all().order_by('-date')
        paginator = Paginator(news_list, 6)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        context = {'news': news, 'page_obj': page_obj}
        return render(request, 'myapp/news.html', context)
