# Generated by Django 3.2.12 on 2022-09-02 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20220831_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='sifre',
            field=models.CharField(max_length=50, null=True, verbose_name='Şifre'),
        ),
    ]
