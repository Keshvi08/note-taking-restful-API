# Generated by Django 4.2.7 on 2023-11-09 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_customusercreationform_alter_notes_modified_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUserCreationForm',
        ),
    ]