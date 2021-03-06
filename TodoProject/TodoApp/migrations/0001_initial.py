# Generated by Django 3.1 on 2020-08-16 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Not-Started', 'Not Started'), ('In-Progress', 'In Progress'), ('Complete', 'Complete')], max_length=12)),
            ],
        ),
    ]
