# Generated by Django 3.2.16 on 2023-07-02 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='uploads/')),
                ('document_url', models.URLField()),
                ('num_page', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
