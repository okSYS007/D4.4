# Generated by Django 4.0.5 on 2022-06-14 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_rename_user_rate_author_author_rate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_choice',
            field=models.CharField(choices=[(1, 'Статья'), (2, 'Новость')], default=1, max_length=2),
        ),
    ]