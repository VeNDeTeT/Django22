from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    content = models.TextField('Содержимое')
    preview = models.ImageField('Превью', upload_to='blog/previews/', blank=True)
    created_at = models.DateTimeField('Дата создания', default=timezone.now)
    is_published = models.BooleanField('Опубликовано', default=True)
    views_count = models.PositiveIntegerField('Просмотры', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись блога'
        verbose_name_plural = 'Записи блога'
