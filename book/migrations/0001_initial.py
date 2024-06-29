# Generated by Django 5.0.6 on 2024-06-29 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('count', models.PositiveIntegerField()),
                ('price', models.FloatField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
