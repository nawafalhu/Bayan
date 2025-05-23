# Generated by Django 3.2.22 on 2025-02-05 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_dictionary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('video_file', models.FileField(upload_to='videos/')),
            ],
        ),
    ]
