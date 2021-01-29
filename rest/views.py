from django.shortcuts import render
from django.http import JsonResponse
from .models import Photo, Folder
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PhotoSerializer, FolderSerializer

# Create your views here.


def restView(request):
    return JsonResponse({'key': 'value'}, safe=False)


@api_view(['GET'])
def photos(req):
    photos = Photo.objects.all()
    serializer = PhotoSerializer(photos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def folders(req):
    folders = Folder.objects.all()
    serializer = FolderSerializer(folders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def folderPhotos(req, id):
    photos = get_object_or_404(Folder, id=id).allPhotos.all()
    serializer = PhotoSerializer(photos, many=True)
    return Response(serializer.data)
