# Generated by Django 3.2.9 on 2021-12-08 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0009_auto_20211208_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='followers', to='insta.Post'),
        ),
    ]