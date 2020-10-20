# in python 3: from io import StringIO
from django.test import TestCase, Client
from myapp.models import News
from django.core.files import File


class ViewsTestCase(TestCase):
    def setUp(self):
        self.news = News.objects.create(title="Первая новость",
                                        description='Эта новость первая',
                                        image=File(open('myapp/tests/img/1.jpg',
                                                        'rb')))
        self.news2 = News.objects.create(title="Вторая новость",
                                         description='Эта новость вторая',
                                         image=File(
                                             open('myapp/tests/img/1.jpg',
                                                  'rb')))
        self.news3 = News.objects.create(title="Третья новость",
                                         description='Эта новость третья',
                                         image=File(
                                             open('myapp/tests/img/1.jpg',
                                                  'rb')))

    def test_news_list_view(self):
        client = Client()
        response = client.get('/news-list/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context['news_dir'].values()),
                         [list(News.objects.all().order_by('-date'))])
        self.assertTemplateUsed(response, 'myapp/news-list.html')

    def test_news_info(self):
        client = Client()
        response = client.get('/news/' + f"{self.news.id}" + '/')
        self.assertEqual(response.context['news'].title, self.news.title)
        self.assertEqual(response.context['news'].description,
                         self.news.description)
        self.assertEqual(response.context['news'].image, self.news.image)
        self.assertEqual(response.status_code, 200)
