# Generated by Django 5.0.6 on 2024-05-25 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordModle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.CharField(max_length=700)),
                ('username', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=600)),
                ('remarks', models.CharField(max_length=5000)),
            ],
        ),
    ]
