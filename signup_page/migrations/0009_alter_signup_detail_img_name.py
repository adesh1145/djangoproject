# Generated by Django 4.0.4 on 2022-05-15 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup_page', '0008_alter_signup_detail_img_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup_detail',
            name='img_name',
            field=models.FileField(default='', max_length=500, null=True, upload_to='upload_file'),
        ),
    ]
