# Generated by Django 4.0 on 2022-02-14 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dental', '0003_blog_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Dental.categories'),
            preserve_default=False,
        ),
    ]
