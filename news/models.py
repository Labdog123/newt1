from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Post(models.Model):
    CATEGORY_CHOICES = (('International', 'international'),
                        ('Local', 'local'),
                        ('Politics', 'politics'),
                        ('Agriculture', 'agriculture'),
                        ('Oil', 'oil'),
                        ('Finance', 'Finance'),
                        ('Health', 'health'),
                        ('Sports', 'sports'),
                        ('Fashion', 'fashion'),
                        ('Tech', 'tech'),
                        ('Weather', 'weather'))

    STATUS_CHOICES = (
        ('Published', 'published'),
        ('Drafted', 'drafted')
    )

    title = models.CharField(max_length=200)

    body = models.TextField()

    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)

    date_published = models.DateTimeField(default=timezone.now)

    date_updated = models.DateTimeField(auto_now=True)

    post_image = models.FileField(null=True, blank=True)

    status = models.CharField(max_length=200,
                              choices=STATUS_CHOICES,
                              default='Drafted')

    category = models.CharField(Category, max_length=100, null=True, blank=True, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail',
                       args=[self.pk])

    class Meta:
        ordering = ('date_published',)

class Reader(models.Model):
    name = models.CharField(max_length=100)
    fav_tag = models.CharField(Category, max_length=100)
    starred = models.ForeignKey(Post,
                                on_delete=models.CASCADE,
                                related_name='starred')
    history = models.ForeignKey(Post,
                                on_delete=models.CASCADE,
                                related_name='history')

    def __str__(self):
        return self.name

