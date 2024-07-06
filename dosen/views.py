from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Dosen
from .serializers import DosenSerializer

@api_view(['GET', 'POST'])
def dosen_list(request):
    """
    List semua dosen atau buat dosen baru.
    """
    if request.method == 'GET':
        dosen = Dosen.objects.all()
        serializer = DosenSerializer(dosen, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DosenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def dosen_detail(request, pk):
    """
    Ambil, update, atau hapus dosen tertentu.
    """
    dosen = get_object_or_404(Dosen, pk=pk)

    if request.method == 'GET':
        serializer = DosenSerializer(dosen)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DosenSerializer(dosen, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        dosen.delete()
        return Response(status=204)
