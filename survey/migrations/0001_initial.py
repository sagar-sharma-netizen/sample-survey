# Generated by Django 3.1.1 on 2021-07-27 14:36

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
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified At')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is deleted instance')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active instance')),
                ('question', models.CharField(db_index=True, max_length=256, unique=True, verbose_name='Category Name')),
                ('details', models.CharField(blank=True, max_length=256, verbose_name='Category Details')),
                ('answer_type', models.CharField(choices=[('int', 'Integer'), ('str', 'String')], default='str', max_length=256)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified At')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is deleted instance')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active instance')),
                ('reporter_name', models.CharField(db_index=True, max_length=256, verbose_name='Sub Category Name')),
                ('reporter_email', models.CharField(blank=True, db_index=True, max_length=256, verbose_name='Sub Category Details')),
                ('result', models.JSONField(default=dict, verbose_name='Survey Result')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
