# Generated by Django 3.0.5 on 2020-04-27 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.CharField(default='no image, text to owner to update info', max_length=10000),
        ),
        migrations.AddField(
            model_name='book',
            name='link',
            field=models.CharField(default='No inforamtion, text to owner to update info', max_length=10000),
        ),
    ]
