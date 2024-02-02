from .views import ShortenUrlView

from django.urls import path, include

from rest_framework.routers import DefaultRouter

app_name = 'url_shortener_api'

router = DefaultRouter(trailing_slash=False)

router.register(
    r"", ShortenUrlView, basename="url-shortener",
)

urlpatterns = [
    path('shorten', ShortenUrlView.as_view({'post': 'shorten_url'}), name='shorten-url'),
    path('<short_code>/stats', ShortenUrlView.as_view({'get': 'get_shortened_url_stats'}), name='get-url-stats'),
    path('<short_code>', ShortenUrlView.as_view({'get': 'access_shortened_url'}), name='access-shortened-url'),
]
