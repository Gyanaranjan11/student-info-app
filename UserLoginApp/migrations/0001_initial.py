# Generated by Django 3.2.3 on 2022-01-08 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]