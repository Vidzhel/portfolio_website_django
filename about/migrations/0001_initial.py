# Generated by Django 2.2.4 on 2019-08-12 09:46

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
                ('about', models.TextField()),
                ('about_img', models.ImageField(blank=True, help_text='Select image for this section', null=True, upload_to='about/images')),
                ('education', models.TextField()),
                ('work_experience', models.TextField()),
                ('honors', models.TextField()),
                ('developer_skills', models.TextField()),
                ('designer_skills', models.TextField()),
            ],
        ),
    ]
