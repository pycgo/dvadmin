from django.conf import settings

# 注册app
app = 'plugins.plugins_market_backend'
if app not in settings.MIDDLEWARE:
    settings.INSTALLED_APPS += [app]
