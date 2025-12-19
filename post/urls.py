from django.urls import path
from .views import home_page, post_create, post_create_view

urlpatterns = [
    path('', home_page, name='home'),
    path ('post-create/', post_create, name="create-post"),
    path('post/create/', post_create_view, name="post-create-view"),
]


