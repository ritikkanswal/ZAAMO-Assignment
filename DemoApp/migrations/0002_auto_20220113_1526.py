# Generated by Django 3.2.6 on 2022-01-13 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DemoApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('res_type', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('opens_at', models.CharField(max_length=100)),
                ('close_at', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
