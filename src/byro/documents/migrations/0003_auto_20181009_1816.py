# Generated by Django 2.1.1 on 2018-10-09 18:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_document_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='document',
            options={'ordering': ('-date', 'title', '-id')},
        ),
        migrations.AddField(
            model_name='document',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='content_hash',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(max_length=1000, upload_to='documents/%Y/%m/'),
        ),
    ]
