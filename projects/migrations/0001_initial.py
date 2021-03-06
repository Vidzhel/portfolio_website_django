# Generated by Django 2.2.4 on 2019-08-15 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectItem',
            fields=[
                ('alias', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('img', models.ImageField(help_text='Select image for this project', upload_to='project_item/images')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('in_progress', models.BooleanField(default=False, help_text='Determines if this project currently in progress')),
                ('code_source', models.CharField(help_text="Link on this project's code source", max_length=100)),
                ('about', models.TextField()),
                ('about_img', models.ImageField(blank=True, help_text='Select image for this section', null=True, upload_to='project_item/images')),
                ('project_difficulties', models.TextField(blank=True, null=True)),
                ('project_difficulties_img', models.ImageField(blank=True, help_text='Select image for this section', null=True, upload_to='project_item/images')),
                ('solutions', models.TextField(blank=True, null=True)),
                ('solutions_img', models.ImageField(blank=True, help_text='Select image for this section', null=True, upload_to='project_item/images')),
                ('features', models.TextField(blank=True, help_text='Each item of the list splits on two parts:\n {title%content%endtitle}{items%item1;item2;item3;%enditems}', null=True)),
                ('technologies', models.TextField(blank=True, help_text='Each item of the list splits on two parts:\n {title%content%endtitle}{items%item1;item2;item3;%enditems}', null=True)),
                ('categories', models.ManyToManyField(help_text='Choose categories for this project', to='projects.Category')),
                ('tags', models.ManyToManyField(help_text='Choose tags for this project', to='projects.Tag')),
            ],
            options={
                'ordering': ['-upload_date'],
            },
        ),
    ]
