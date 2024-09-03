# Generated by Django 5.1 on 2024-09-03 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendationAPI', '0002_rename_recommended_book_recommendation_book_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(help_text='Please supply a 13 digit-long ISBN.', max_length=13, unique=True),
        ),
    ]
