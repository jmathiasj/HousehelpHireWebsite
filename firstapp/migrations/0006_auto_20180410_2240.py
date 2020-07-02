# Generated by Django 2.0.3 on 2018-04-10 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_auto_20180410_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accessrecord',
            name='date',
        ),
        migrations.AddField(
            model_name='accessrecord',
            name='number',
            field=models.IntegerField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='accessrecord',
            name='work',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AlterField(
            model_name='accessrecord',
            name='name',
            field=models.CharField(default=0, max_length=200),
        ),
    ]
