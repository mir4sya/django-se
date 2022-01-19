# Generated by Django 3.2.4 on 2021-07-19 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0004_auto_20210711_0158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('qty', models.PositiveIntegerField()),
            ],
        ),
    ]
