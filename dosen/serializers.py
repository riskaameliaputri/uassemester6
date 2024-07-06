from rest_framework import serializers
from .models import Dosen

class DosenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dosen
        fields = ['id', 'nama', 'nip', 'jabatan', 'bidang']
