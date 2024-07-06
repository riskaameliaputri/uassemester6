from django.db import models
from api.models import Mahasiswa
from dosen.models import Dosen

class MataPelajaran(models.Model):
    nama = models.CharField(max_length=100)
    kode = models.CharField(max_length=20)
    deskripsi = models.TextField()
    mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE)
    dosen = models.ForeignKey(Dosen, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama
