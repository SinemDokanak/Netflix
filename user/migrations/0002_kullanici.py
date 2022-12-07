# Generated by Django 3.2.12 on 2022-08-31 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kullanici',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=50)),
                ('soyisim', models.CharField(max_length=50)),
                ('resim', models.FileField(upload_to='kullanıcılar/', verbose_name='Profil resmi')),
                ('tel', models.IntegerField(default=0)),
                ('dogum', models.DateField()),
                ('olusturulma_tarih', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
