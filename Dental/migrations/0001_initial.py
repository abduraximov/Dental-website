# Generated by Django 4.0 on 2022-02-13 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('ex_dentist', models.IntegerField(max_length=40)),
                ('mod_equip', models.IntegerField(max_length=40)),
                ('friendly_staff', models.IntegerField(max_length=40)),
                ('exp_year', models.IntegerField(max_length=40)),
                ('happy_patients', models.IntegerField(max_length=40)),
                ('certificate', models.IntegerField(max_length=40)),
            ],
        ),
    ]