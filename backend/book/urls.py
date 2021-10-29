from django.urls import path, re_path
from rest_framework import routers

from book.views import BookViewSet



book_url = routers.SimpleRouter()
book_url.register(r'book', BookViewSet)

urlpatterns = []
urlpatterns += book_url.urls