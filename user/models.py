from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profiles(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    isim = models.CharField(max_length = 50, verbose_name = 'İsim')
    resim = models.FileField(upload_to = 'profiles/', verbose_name='Profil Resmi')
    sifre = models.CharField(max_length = 50, verbose_name = 'Şifre', null=True)
    def __str__(self):
        return self.isim

class Kullanici(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    isim = models.CharField(max_length=50)
    soyisim = models.CharField(max_length=50)
    email = models.CharField(max_length=100, null=True)
    resim = models.FileField(upload_to='kullanicilar/', verbose_name='Profil resmi')
    tel = models.IntegerField(default=0)
    date = models.DateField(null=True)
    olusturulma_tarih = models.DateField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.isim
