from django.urls import path, re_path

from .views import *

urlpatterns = [
    path("", index, name='home'),
    path("about/", about, name='about'),
    path('content/', content, name='content'),
    # path('addpage/', addpage, name='add_page'),
    path('comment/', comment, name='comment'),
    path('contact/', contact, name='contact'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category')
]