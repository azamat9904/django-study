from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Наименование")
    content = models.TextField(blank=True, verbose_name="Текст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создание")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата редактирование")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name="Изображение", blank=True)
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["created_at"]


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Наименование категории", db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['title']


#6,16,29