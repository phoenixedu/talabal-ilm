from typing import Any
from django.http import HttpRequest, HttpResponse
from .forms import BlogPostForm,DefaltBlogPostForm
from .models import BlogPost,Comment,DefaltBlogPost
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View,DetailView,ListView,UpdateView,DeleteView
from django.contrib.auth.models import User
from django.urls import reverse_lazy


# view
class createBlogPostUser(View):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blogs/createUserBlogs.html'
    def get(self,request):
        if request.user.is_authenticated:
            form = self.form_class()
            return render(request,self.template_name,{'form':form})
        else:
            return redirect('home')
    def post(self,request):
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('BlogPD', instance.uuid)
        return render(request,self.template_name,{'form':form})
    
class blogPostDetile(DetailView):
    model = BlogPost
    template_name = "blogs/blogPost.html"
    context_object_name = "blogP"

    def get(self,request,uuid):
        blogP = get_object_or_404(BlogPost,uuid=uuid)
        comments = Comment.objects.filter(blog_post=blogP)
        blogs_list = BlogPost.objects.filter(author=blogP.author)
        blogP.views += 1
        blogP.save()
        contx = {
            'comments':comments,
            'blogs_list':blogs_list,
            self.context_object_name : blogP,
        }
        return render(request,self.template_name,contx)
    def post(self,request,uuid):
        blogP = get_object_or_404(BlogPost,uuid=uuid)
        comment = request.POST.get('content')
        if request.user.is_authenticated:
            Comment.objects.create(
                blog_post = blogP,
                author_name = request.user,
                content = comment,
            )
        else:
            pass
        return redirect(request.path)

class allBlogsList(ListView):
    model = BlogPost
    template_name = "blogs/allBlogs.html"
    context_object_name = "blogs_list"

    def get(self,request):
        if request.user.is_authenticated:
            blogs_list = BlogPost.objects.filter(author=request.user)
            contx = {
                self.context_object_name:blogs_list,
            }
            return render(request,self.template_name,contx)
        else:
            return redirect('home')

class updateBlogPost(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = "blogs/editBlogPost.html"
    context_object_name = "blog"

    def get(self,request,uuid):
        blog = get_object_or_404(BlogPost,uuid=uuid)
        if request.user == blog.author:
            form = self.form_class(instance=blog) 
            contx = {
                'blog':blog,
                'form':form,
            }
            return render(request,self.template_name,contx)
        else:
            return redirect('BlogPD' , uuid=blog.uuid )
    def post(self, request,uuid):
        blog = get_object_or_404(BlogPost,uuid=uuid)
        form = self.form_class(request.POST,request.FILES,instance=blog)
        if form.is_valid():
            form.save()
            return redirect('BlogPD' , uuid=blog.uuid)
        contx = {
            'blog':blog,
            'form':form,
        }
        return render(request,self.template_name,contx)
        
    
class DeleteBlogPost(DeleteView):
    model = BlogPost
    template_name = "blogs/trash.html"
    success_url = reverse_lazy('bloglist') 
    def get_object(self, queryset=None):
        uuid = self.kwargs.get('uuid')
        return get_object_or_404(BlogPost, uuid=uuid)

    def post(self, request, *args, **kwargs):
        blog_post = self.get_object()
        if request.user == blog_post.author:
            blog_post.delete()
        return redirect(self.success_url)

class updateDefaltBlogPost(UpdateView):
    model = DefaltBlogPost
    form_class = DefaltBlogPostForm
    template_name = "blogs/defaultPostUpdate.html"
    context_object_name = 'dfl_blog'
    def get(self,request,pk,key):
        dfl_blog = get_object_or_404(DefaltBlogPost,pk=pk,key=key)
        form = self.form_class(instance=dfl_blog)
        contx = {
            self.context_object_name:dfl_blog,
            'form':form,
        }
        return render(request,self.template_name,contx)
    def post(self,request,pk,key):
        dfl_blog = get_object_or_404(DefaltBlogPost,pk=pk,key=key)
        form = self.form_class(request.POST,instance=dfl_blog)
        if form.is_valid():
            form.save()
            return redirect('home')
        contx = {
            self.context_object_name:dfl_blog,
            'form':form,
        }
        return render(request,self.template_name,contx)


        