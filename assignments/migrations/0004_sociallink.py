# Generated by Django 4.2.5 on 2023-10-03 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0003_rename_abount_description_about_about_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=25)),
                ('link', models.URLField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
