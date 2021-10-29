# -*- coding: utf-8 -*-
from django.urls import re_path
from rest_framework import routers

from plugins.plugins_market_backend.views import PluginsMarketViewSet

system_url = routers.SimpleRouter()
# system_url.register(r'menu', MenuViewSet)

urlpatterns = [
    re_path('plugins', PluginsMarketViewSet.as_view({'get': 'list','post': 'create','put': 'update','delete': 'delete'})),
]
urlpatterns += system_url.urls
