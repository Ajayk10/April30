# Generated by Django 3.1.1 on 2021-01-14 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('April30', '0002_auto_20210114_1112'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answers4',
            old_name='i13',
            new_name='i17',
        ),
        migrations.RemoveField(
            model_name='answers5',
            name='i17',
        ),
        migrations.AddField(
            model_name='answers3',
            name='i13',
            field=models.TextField(null=True),
        ),
    ]