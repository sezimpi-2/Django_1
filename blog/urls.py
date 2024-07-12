from django.contrib import admin
from django.urls import path
from post.views import post_view, main_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', post_view),
    path('', main_page),
]
