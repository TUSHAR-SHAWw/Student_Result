# Generated by Django 4.2.7 on 2023-12-20 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student_app', '0010_alter_rank_creaton_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rank',
            name='creaton_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
