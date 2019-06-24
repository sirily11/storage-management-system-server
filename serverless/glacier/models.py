from django.db import models


class Glacier(models.Model):
    access_id = models.CharField(verbose_name="AWS Access ID", max_length=255, default="", unique=True)

    def __str__(self):
        return self.access_id


class Vault(models.Model):
    glacier = models.ForeignKey(to=Glacier,
                                verbose_name="Glacier account",
                                on_delete=models.CASCADE,
                                related_name="vaults")
    created_at = models.DateTimeField(auto_now_add=True)
    VaultName = models.CharField(verbose_name="Vault Name", max_length=255, default="", unique=True)

    def __str__(self):
        return f"{self.VaultName} - {self.glacier.access_id}"


class File(models.Model):
    vault = models.ForeignKey(to=Vault,
                              verbose_name="File",
                              related_name="files",
                              on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    filename = models.CharField(max_length=1024)
    filesize = models.FloatField(verbose_name="File Size (bytes)")
    achieveId = models.CharField(max_length=1024)

    def __str__(self):
        return self.filename
