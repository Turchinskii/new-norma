from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='myapp/images', blank=True,default=None,
                              verbose_name='Изображение')

    class Meta:
        verbose_name = ('новость')
        verbose_name_plural = ('новости')

    def __str__(self):
        return self.title
