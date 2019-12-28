# Generated by Django 2.1.4 on 2019-12-12 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_title', models.CharField(max_length=200)),
                ('question_content', models.TextField()),
                ('question_opt1', models.CharField(max_length=200)),
                ('question_opt2', models.CharField(max_length=200)),
                ('question_opt3', models.CharField(max_length=200)),
                ('question_opt4', models.CharField(max_length=200)),
                ('question_ans', models.CharField(max_length=200)),
            ],
        ),
    ]