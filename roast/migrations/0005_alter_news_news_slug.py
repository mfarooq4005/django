# Generated by Django 4.2.4 on 2023-09-05 02:59

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roast', '0004_news_news_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='news_title', unique=True),
        ),
    ]
