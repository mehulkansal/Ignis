# Generated by Django 3.1.7 on 2021-09-12 12:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('location', models.CharField(max_length=40)),
                ('time', models.DateTimeField()),
                ('Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Name', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]