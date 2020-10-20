from django.urls import path
from myapp.views import NewsListView, NewsInfoView

urlpatterns = [
    path('news-list/', NewsListView.as_view(), name='news-list'),
    path('news/<int:pk>/', NewsInfoView.as_view(), name='news-info'),
]
