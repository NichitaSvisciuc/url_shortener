from rest_framework.test import (
    APIRequestFactory,
    APITestCase,
    APIClient,
)

from django.urls import reverse

from .models import ShortenedUrl


api_client = APIClient()
factory = APIRequestFactory()


class TestShortenUrlView(APITestCase):
    def setUp(self):
        self.default_shortened_url = ShortenedUrl.objects.create(
            url='https://www.google.com/', shortcode='google'
        )

    def test_shortened_url_creation(self):
        url_name = 'url_shortener_api:shorten-url'
        short_code = 'abc123'
        original_url = 'https://www.google.com/'
        data = {
            'url': original_url,
            'shortcode': short_code
        }

        response = self.client.post(reverse(url_name), data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['url'], original_url)
        self.assertEqual(response.data['shortcode'], short_code)

    def test_duplicate_url_creation(self):
        url_name = 'url_shortener_api:shorten-url'
        short_code = 'google'
        original_url = 'https://www.google.com/'
        data = {
            'url': original_url,
            'shortcode': short_code
        }

        response = self.client.post(reverse(url_name), data)
        self.assertEqual(response.status_code, 400)

    def test_get_url_stats(self):
        url_name = 'url_shortener_api:get-url-stats'

        response = self.client.get(reverse(url_name, kwargs={'short_code': self.default_shortened_url.shortcode}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['redirect_count'], 0)

    def test_url_not_found(self):
        url_name = 'url_shortener_api:get-url-stats'

        response = self.client.get(reverse(url_name, kwargs={'short_code': '1'}))
        self.assertEqual(response.status_code, 404)

    def test_shortened_url_access(self):
        url_name = 'url_shortener_api:access-shortened-url'

        response = self.client.get(reverse(url_name, kwargs={'short_code': self.default_shortened_url.shortcode}))
        self.assertEqual(response.status_code, 302)

    def test_shortened_url_validations(self):
        url_name = 'url_shortener_api:shorten-url'
        invalid_short_code = 'abc12367'
        original_url = 'https://www.google.com/'
        data = {
            'url': original_url,
            'shortcode': invalid_short_code
        }

        response = self.client.post(reverse(url_name), data)
        self.assertEqual(response.status_code, 400)

        del data['url']
        response = self.client.post(reverse(url_name), data)
        self.assertEqual(response.status_code, 400)
