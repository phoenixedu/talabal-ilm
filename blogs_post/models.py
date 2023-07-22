from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from edu.models import xEduInstitution
import uuid
import random
import os

def upload_path(instance, filename):
    ext = filename.split('.')[-1]
    random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(4))
    filename = f'{instance.title}-{instance.uuid}-{random_numbers}.{ext}'
    return os.path.join('images/blogs', filename)

class tags(models.Model):
    name = models.CharField(unique=True, blank=True,null=True,max_length=50)
    def __str__(self):
        return self.name


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = RichTextField(blank=True,null=True)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    uuid = models.UUIDField(default=uuid.uuid4,editable=False)
    tags = models.ManyToManyField(tags, blank=True,related_name="blog_tags")

    # meta
    meta_title = models.CharField(max_length=200, blank=True, null=True)
    meta_author = models.CharField(max_length=100, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.CharField(max_length=200, blank=True, null=True)
    featured_image = models.ImageField(upload_to=upload_path, blank=True, null=True)
    
    publication_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    is_publish = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        if not self.meta_title:
            self.meta_title = self.title
        if not self.meta_author:
            self.meta_author = self.author.username
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='blog_coments')
    author_name = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    content = models.TextField()
    likes = models.IntegerField(default=0)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author_name} - {self.blog_post.title} ({self.date_posted})"
    

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Share(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class DefaltBlogPost(models.Model):
    key = models.CharField(max_length=250,blank=True,null=True)
    title = models.CharField(max_length=200,blank=True,null=True)
    content = RichTextField(blank=True,null=True)
    last_updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4,editable=False)
    
    def __str__(self):
        return self.title