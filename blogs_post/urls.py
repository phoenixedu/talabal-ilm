from django.urls import path
from .views import createBlogPostUser,blogPostDetile,allBlogsList,updateBlogPost,updateDefaltBlogPost,DeleteBlogPost

urlpatterns = [
    path('post/create/', createBlogPostUser.as_view(), name='blogForm'),
    path('post/<str:uuid>/', blogPostDetile.as_view(), name='BlogPD'),
    path('posts/', allBlogsList.as_view(), name='bloglist'),
    path('post/edit/<str:uuid>/', updateBlogPost.as_view(), name='editBlogPost'),
    path('post/<str:uuid>/delete/', DeleteBlogPost.as_view(), name='delete_blog_post'),
    path('post/d/<int:pk>/<str:key>/', updateDefaltBlogPost.as_view(), name='defaultPost'),

]
