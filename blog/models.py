from django.db import models
from django.contrib.auth.models import User

class ContactUs(models.Model):

    name = models.CharField(max_length=200, null=False)
    phone = models.CharField(max_length=200, null=False)
    subject = models.CharField(max_length=200, null=False, default="")
    email = models.EmailField(max_length=200, null=False)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Contact Us"
        ordering = ('-created_at',)


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

