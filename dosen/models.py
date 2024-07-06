from django.db import models

class Dosen(models.Model):
    nama = models.CharField(max_length=100)
    nip = models.CharField(max_length=20)
    jabatan = models.CharField(max_length=50)
    bidang = models.CharField(max_length=100)

    def __str__(self):
        return self.nama
