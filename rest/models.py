from django.db import models

# Create your models here.


class Folder(models.Model):
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=3000, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Photo(models.Model):
    folder = models.ForeignKey(
        Folder, on_delete=models.CASCADE, related_name='allPhotos')
    photo = models.FileField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.photo)
