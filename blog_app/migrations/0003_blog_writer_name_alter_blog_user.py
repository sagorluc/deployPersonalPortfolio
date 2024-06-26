# Generated by Django 5.0.5 on 2024-05-09 08:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_blog_short_text'),
        ('profile_app', '0008_remove_myprofile_download_resume_resumedownload'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='writer_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='profile_app.myprofile'),
        ),
    ]
