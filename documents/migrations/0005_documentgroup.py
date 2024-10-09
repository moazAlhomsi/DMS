# Generated by Django 5.1 on 2024-10-04 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0004_document_language_alter_document_file_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('documents', models.ManyToManyField(related_name='groups', to='documents.document')),
            ],
        ),
    ]
