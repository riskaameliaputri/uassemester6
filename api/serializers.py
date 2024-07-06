from rest_framework import serializers
from .models import Mahasiswa

class MahasiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahasiswa
        fields = ['id', 'nama', 'nim', 'jurusan', 'tahun_masuk']
