# Generated by Django 4.0.3 on 2022-03-21 15:28

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=60)),
                ('hoodimage', cloudinary.models.CloudinaryField(max_length=255)),
                ('description', models.CharField(max_length=60)),
                ('police_number', models.IntegerField(blank=True, null=True)),
                ('emergency_no', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(blank=True, max_length=120)),
                ('profile_pic', cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/playboard/image/upload/v1626529829/vjytnast5wblft8xvy9p.jpg', max_length=255)),
                ('full_name', models.CharField(blank=True, max_length=120)),
                ('profession', models.CharField(blank=True, max_length=120)),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True)),
                ('mobile_number', models.IntegerField(blank=True, null=True)),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members', to='area.area')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='area',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin', to='area.profile'),
        ),
    ]
