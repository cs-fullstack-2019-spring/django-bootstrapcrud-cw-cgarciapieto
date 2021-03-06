# Generated by Django 2.2 on 2019-03-08 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.CharField(max_length=200)),
                ('URL', models.URLField()),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=1000)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]
