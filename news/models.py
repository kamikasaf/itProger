from django.db import models

class News(models.Model):

    title = models.CharField(max_length=100, verbose_name='Название')
    anons = models.CharField(max_length=250, verbose_name='Анонс')
    full_text = models.TextField(verbose_name='Статья')
    data = models.DateTimeField(verbose_name='Дата публикации')
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def get_absolute_url(self):
        return f'/news/{self.id}'

    def __str__(self):
        return self.title

    