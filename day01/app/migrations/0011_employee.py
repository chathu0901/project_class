# Generated by Django 5.0.6 on 2024-07-24 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_order_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
