from django.db import models
from django.urls import reverse


class Furniture(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Описание")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время публикации")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категории")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = "Мебель"
        verbose_name_plural = "Мебель"
        ordering = ['id']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категории")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"


class Content(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название статьи")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время публикации")
    is_published = models.BooleanField(default=True, verbose_name="Публикация статьи")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('content', kwargs={'content_slug': self.slug})

    class Meta:
        verbose_name = "Статьи"
        verbose_name_plural = "Статья"
        ordering = ['id']


class Comment(models.Model):
    name = models.CharField(max_length=255, verbose_name="Отзыв")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото отзыва")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время публикации")
    is_published = models.BooleanField(default=True, verbose_name="Публикация статьи")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('comment', kwargs={'comment_slug': self.slug})

    class Meta:
        verbose_name = "Отзывы"
        verbose_name_plural = "Отзывы"
        ordering = ['id']
