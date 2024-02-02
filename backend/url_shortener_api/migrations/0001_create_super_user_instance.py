# Generated by Django 4.1 on 2024-02-01 17:21

from django.db import migrations, models
from django.contrib.auth.hashers import make_password


def create_superuser(apps, schema_editor):
    User = apps.get_model('auth', 'User')

    admin_email = 'admin@mail.com'

    if not User.objects.filter(email=admin_email):
        admin_username = 'admin'
        admin_password = 'admin'

        superuser = User.objects.create(
            username=admin_username,
            email=admin_email,
            password=make_password(admin_password),
            is_superuser=True,
            is_staff=True,
            is_active=True
        )
        superuser.save()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.RunPython(create_superuser)
    ]