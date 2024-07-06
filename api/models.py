from django.db import models

class Mahasiswa(models.Model):
    nama = models.CharField(max_length=100)
    nim = models.CharField(max_length=20)
    jurusan = models.CharField(max_length=50)
    tahun_masuk = models.IntegerField()

    def __str__(self):
        return self.nama
