# Generated by Django 4.1.7 on 2023-03-27 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_event_tag_remove_tag_content_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='Article',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='audiobooks',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='books',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='works',
        ),
    ]
