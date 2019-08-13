# Generated by Django 2.2.4 on 2019-08-13 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20190812_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='designer_skills',
            field=models.TextField(blank=True, help_text='Each item of the list splits on two parts:\n {title%content%endtitle}{items%item1;item2;item3;%enditems}', null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='developer_skills',
            field=models.TextField(blank=True, help_text='Each item of the list splits on two parts:\n {title%content%endtitle}{items%item1;item2;item3;%enditems}', null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='education',
            field=models.TextField(blank=True, help_text='Each item of the article splits on three parts:\n {title%content%endtitle}{years%content%endyears}{text%content%endtext}', null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='honors',
            field=models.TextField(blank=True, help_text='Each item of the article splits on three parts:\n {title%content%endtitle}{years%content%endyears}{text%content%endtext}', null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='work_experience',
            field=models.TextField(blank=True, help_text='Each item of the article splits on three parts:\n {title%content%endtitle}{years%content%endyears}{text%content%endtext}', null=True),
        ),
    ]
