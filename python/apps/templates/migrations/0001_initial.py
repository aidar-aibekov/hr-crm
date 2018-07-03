# Generated by Django 2.0.6 on 2018-07-02 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('type', models.CharField(max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'default_related_name': 'attachments',
            },
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=1000)),
                ('type', models.CharField(max_length=10)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('attachments', models.ManyToManyField(related_name='templates', to='templates.Attachment')),
            ],
            options={
                'default_related_name': 'templates',
            },
        ),
    ]