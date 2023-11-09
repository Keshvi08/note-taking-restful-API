# Generated by Django 4.2.7 on 2023-11-08 13:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_remove_notes_created_remove_notes_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='notes',
            name='modified_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]