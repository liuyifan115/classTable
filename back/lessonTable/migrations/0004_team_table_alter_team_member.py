# Generated by Django 4.1.1 on 2022-09-17 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessonTable', '0003_team_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='table',
            field=models.CharField(default='[]', max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='member',
            field=models.CharField(default='[]', max_length=100),
        ),
    ]
