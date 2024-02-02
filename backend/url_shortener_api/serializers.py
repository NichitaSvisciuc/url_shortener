from rest_framework import serializers

from .models import ShortenedUrl
from .constants import DEFAULT_RANDOM_SHORTENED_STRING_LENGTH


class ShortenUrlSerializer(serializers.ModelSerializer):
    url = serializers.URLField()

    class Meta:
        model = ShortenedUrl
        fields = [
            'url',
            'shortcode'
        ]

    def validate(self, attrs):
        short_code = attrs.get('shortcode') or ''
        original_url = attrs.get('url', None)

        self.validate_short_code_length(short_code)
        self.validate_original_url(original_url)
        self.validate_short_code_uniqueness(short_code)

        return super().validate(attrs)

    def validate_short_code_length(self, short_code):
        if len(short_code) > 6:
            raise serializers.ValidationError(
                f'Not Valid : Short code length should not be more than {DEFAULT_RANDOM_SHORTENED_STRING_LENGTH} chars'
            )

    def validate_original_url(self, original_url):
        if original_url is None:
            raise serializers.ValidationError(
                f'Url not present'
            )

    def validate_short_code_uniqueness(self, shortcode):
        short_code = ShortenedUrl.objects.filter(shortcode=shortcode)
        if short_code.exists():
            raise serializers.ValidationError(
                'Shortcode already in use'
            )


class ShortenedUrlDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortenedUrl
        fields = [
            'created',
            'last_redirect',
            'redirect_count'
        ]
