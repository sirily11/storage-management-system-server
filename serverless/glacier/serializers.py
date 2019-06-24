from rest_framework import serializers
from .models import Glacier, Vault, File


class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = File
        fields = ("created_at", "filename", "filesize", "achieveId")


class VaultSerializer(serializers.HyperlinkedModelSerializer):
    files = FileSerializer(read_only=True, many=True)

    class Meta:
        model = Vault
        fields = ("VaultName", "created_at", "files")


class GlacierSerializer(serializers.HyperlinkedModelSerializer):
    vaults = VaultSerializer(read_only=True, many=True)

    class Meta:
        model = Glacier
        fields = ("access_id", "vaults")
