# Generated by Django 4.2.2 on 2023-06-27 15:50

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
            name='Welfare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField()),
                ('start_time', models.TimeField(null=True)),
                ('end_time', models.TimeField(null=True)),
                ('address', models.CharField(max_length=30)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('category_univ', models.CharField(blank=True, max_length=50)),
                ('category_type', models.CharField(blank=True, max_length=50)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='welfare/')),
                ('welfare_like_count', models.PositiveIntegerField(default=0)),
                ('welfare_like', models.ManyToManyField(blank=True, related_name='welfare_likes', to=settings.AUTH_USER_MODEL)),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('comment_like_count', models.IntegerField(default=0)),
                ('comment_like', models.ManyToManyField(blank=True, related_name='Welfarecomment_likes', to=settings.AUTH_USER_MODEL)),
                ('welfare', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='welfare.welfare')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
