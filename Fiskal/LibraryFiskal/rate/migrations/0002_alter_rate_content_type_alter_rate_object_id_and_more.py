# Generated by Django 4.1.7 on 2023-03-25 11:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='object_id',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='rate',
            name='rating',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='rate',
            unique_together={('user', 'content_type', 'object_id')},
        ),
        migrations.RemoveField(
            model_name='rate',
            name='created_at',
        ),
    ]
