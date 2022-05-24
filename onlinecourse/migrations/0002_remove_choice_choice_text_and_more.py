# Generated by Django 4.0.4 on 2022-05-24 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='choice_text',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_text',
        ),
        migrations.AddField(
            model_name='choice',
            name='text',
            field=models.CharField(default='choice', max_length=200),
        ),
        migrations.AddField(
            model_name='question',
            name='text',
            field=models.CharField(default='question', max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='grade',
            field=models.FloatField(default=0),
        ),
    ]
