# Generated by Django 4.2.5 on 2023-09-15 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0003_socialmedialink'),
    ]

    operations = [
        migrations.RenameField(
            model_name='socialmedialink',
            old_name='instagrame',
            new_name='github',
        ),
        migrations.AddField(
            model_name='socialmedialink',
            name='instagram',
            field=models.URLField(blank=True, null=True),
        ),
    ]
