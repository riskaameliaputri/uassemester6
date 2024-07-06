from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Mahasiswa
from .serializers import MahasiswaSerializer


@api_view(['GET', 'POST'])
def mahasiswa_list(request):
    """
    List semua mahasiswa atau buat mahasiswa baru.
    """
    if request.method == 'GET':
        mahasiswa = Mahasiswa.objects.all()
        serializer = MahasiswaSerializer(mahasiswa, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MahasiswaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def mahasiswa_detail(request, pk):
    """
    Ambil, update, atau hapus mahasiswa tertentu.
    """
    mahasiswa = get_object_or_404(Mahasiswa, pk=pk)

    if request.method == 'GET':
        serializer = MahasiswaSerializer(mahasiswa)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MahasiswaSerializer(mahasiswa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        mahasiswa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
