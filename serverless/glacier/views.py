from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import status


# Create your views here.
class GlacierViewSet(viewsets.ViewSet):
    def create(self, request):
        try:
            access_key = request.data['access_id']
            print(access_key)

            glacier = Glacier(access_id=access_key)
            glacier.save()
            return Response(status.HTTP_201_CREATED)
        except Exception as e:
            return Response(status.HTTP_400_BAD_REQUEST)

    def list(self, request, **kwargs):
        access_id = request.GET['access_id']
        if not Glacier.objects.filter(access_id=access_id).exists():
            return Response(status.HTTP_404_NOT_FOUND)
        glacier = Glacier.objects.get(access_id=access_id)
        return Response(GlacierSerializer(glacier).data)


class VaultViewSet(viewsets.ViewSet):
    def create(self, request):
        try:
            access_key = request.data['access_id']
            vault_name = request.data['vault_name']
            glacier = Glacier.objects.get(access_id=access_key)
            vault = Vault(VaultName=vault_name, glacier=glacier)
            vault.save()
            return Response(status.HTTP_201_CREATED)
        except Exception as e:
            return Response(status.HTTP_400_BAD_REQUEST)


class FileViewSet(viewsets.ViewSet):
    def create(self, request):
        access_key = request.data['access_id']
        vault_name = request.data['vault_name']
        filename = request.data['filename']
        file_size = request.data['file_size']
        achieve_id = request.data['achieve_id']
        glacier = Glacier.objects.get(access_id=access_key)
        if not Vault.objects.filter(VaultName=vault_name).exists():
            vault = Vault(VaultName=vault_name, glacier=glacier)
            vault.save()
        else:
            vault = Vault.objects.get(glacier=glacier, VaultName=vault_name)
        file = File(vault=vault, filename=filename, filesize=file_size, achieveId=achieve_id)
        file.save()
        return Response(status.HTTP_201_CREATED)
