from django.apps import AppConfig


class PluginsMarketBackendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'plugins.plugins_market_backend'
    url_prefix = "plugins_market",
