from django.contrib import admin
from .models import BlogPost,Comment,tags,DefaltBlogPost
# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Comment)
admin.site.register(tags)
admin.site.register(DefaltBlogPost)