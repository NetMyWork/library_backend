# Generated by Django 4.1.7 on 2023-03-27 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('core', '0002_auto_20230325_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='audiobook',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='book',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='work',
            name='tag',
        ),
        migrations.AddField(
            model_name='tag',
            name='content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='tag',
            name='object_id',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
