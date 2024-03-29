# Generated by Django 4.1 on 2024-02-01 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('url_shortener_api', '0001_create_super_user_instance'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShortenedUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, null=True)),
                ('shortcode', models.CharField(blank=True, max_length=6, null=True, unique=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('last_redirect', models.DateTimeField(blank=True, null=True)),
                ('redirect_count', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'verbose_name': 'Shortened Url',
                'verbose_name_plural': 'Shortened Urls',
            },
        ),
    ]
