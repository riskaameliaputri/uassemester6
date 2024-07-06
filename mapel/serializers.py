from rest_framework import serializers
from api.models import Mahasiswa
from dosen.models import Dosen
from .models import MataPelajaran

class MataPelajaranSerializer(serializers.ModelSerializer):
    mahasiswa = serializers.PrimaryKeyRelatedField(queryset=Mahasiswa.objects.all())
    dosen = serializers.PrimaryKeyRelatedField(queryset=Dosen.objects.all())

    class Meta:
        model = MataPelajaran
        fields = ['id', 'nama', 'kode', 'deskripsi', 'mahasiswa', 'dosen']

    def create(self, validated_data):
        mahasiswa_id = validated_data.pop('mahasiswa').id  # Ambil ID dari objek Mahasiswa
        dosen_id = validated_data.pop('dosen').id  # Ambil ID dari objek Dosen
        mapel = MataPelajaran.objects.create(mahasiswa_id=mahasiswa_id, dosen_id=dosen_id, **validated_data)
        return mapel

    def update(self, instance, validated_data):
        mahasiswa_id = validated_data.pop('mahasiswa').id  # Ambil ID dari objek Mahasiswa yang baru
        dosen_id = validated_data.pop('dosen').id  # Ambil ID dari objek Dosen yang baru

        instance.nama = validated_data.get('nama', instance.nama)
        instance.kode = validated_data.get('kode', instance.kode)
        instance.deskripsi = validated_data.get('deskripsi', instance.deskripsi)
        instance.mahasiswa_id = mahasiswa_id  # Update ID Mahasiswa
        instance.dosen_id = dosen_id  # Update ID Dosen
        instance.save()

        return instance
