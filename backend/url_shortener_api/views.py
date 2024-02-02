from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response

from django.shortcuts import redirect
from django.db.models import ObjectDoesNotExist

from drf_yasg.utils import swagger_auto_schema, no_body

from .serializers import ShortenUrlSerializer, ShortenedUrlDetailSerializer
from .models import ShortenedUrl


class ShortenUrlView(ViewSet):
    queryset = ShortenedUrl.objects.all()
    allowed_methods = ['get', 'post']

    serializers = {
        'GET': ShortenedUrlDetailSerializer,
        'POST': ShortenUrlSerializer
    }

    def get_serializer(self, request):
        return self.serializers[request.method]

    @swagger_auto_schema(request_body=ShortenedUrlDetailSerializer)
    def shorten_url(self, request):
        serializer = self.get_serializer(request)(data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema()
    def access_shortened_url(self, request, **kwargs):
        try:
            url_by_short_code = self.queryset.get(shortcode=kwargs['short_code'])
            url_by_short_code.update_url_stats()
            return redirect(url_by_short_code.url)
        except ObjectDoesNotExist:
            return Response('Shortcode not found', status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema()
    def get_shortened_url_stats(self, request, **kwargs):
        try:
            url_by_short_code = self.queryset.get(shortcode=kwargs['short_code'])
            serializer = self.get_serializer(request)(url_by_short_code, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response('Shortcode not found', status=status.HTTP_404_NOT_FOUND)
