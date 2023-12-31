# Generated by Django 4.2 on 2023-06-15 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiktok', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.CharField(max_length=50)),
                ('link', models.URLField()),
                ('status', models.BooleanField()),
                ('order_likes_id', models.CharField(max_length=50)),
                ('order_views_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
