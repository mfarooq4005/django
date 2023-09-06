# Generated by Django 4.2.4 on 2023-09-04 04:57

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roast', '0003_rename_title_news_news_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from=models.CharField(max_length=100), unique=True),
        ),
    ]