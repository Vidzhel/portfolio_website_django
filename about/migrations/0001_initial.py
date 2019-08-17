# Generated by Django 2.2.4 on 2019-08-15 04:30

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
                ('education', models.TextField(blank=True, help_text='Each item of the article splits on three parts:\n {title%content%endtitle}{years%content%endyears}{text%content%endtext}', null=True)),
                ('work_experience', models.TextField(blank=True, help_text='Each item of the article splits on three parts:\n {title%content%endtitle}{years%content%endyears}{text%content%endtext}', null=True)),
                ('honors', models.TextField(blank=True, help_text='Each item of the article splits on three parts:\n {title%content%endtitle}{years%content%endyears}{text%content%endtext}', null=True)),
                ('developer_skills', models.TextField(blank=True, help_text='Each item of the list splits on two parts:\n {title%content%endtitle}{items%item1;item2;item3;%enditems}', null=True)),
                ('designer_skills', models.TextField(blank=True, help_text='Each item of the list splits on two parts:\n {title%content%endtitle}{items%item1;item2;item3;%enditems}', null=True)),
            ],
        ),
    ]
