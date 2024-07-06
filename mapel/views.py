from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MataPelajaran
from .serializers import MataPelajaranSerializer

@api_view(['GET', 'POST'])
def mapel_list(request):
    """
    List semua mata pelajaran atau buat mata pelajaran baru.
    """
    if request.method == 'GET':
        mapel = MataPelajaran.objects.all()
        serializer = MataPelajaranSerializer(mapel, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MataPelajaranSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def mapel_detail(request, pk):
    """
    Ambil, update, atau hapus mata pelajaran tertentu.
    """
    mapel = get_object_or_404(MataPelajaran, pk=pk)

    if request.method == 'GET':
        serializer = MataPelajaranSerializer(mapel)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MataPelajaranSerializer(mapel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        mapel.delete()
        return Response(status=204)
