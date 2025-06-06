# Generated by Django 5.1.3 on 2025-05-12 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_alter_services_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(default='This is default content')),
                ('image', models.ImageField(upload_to='services_images/')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
