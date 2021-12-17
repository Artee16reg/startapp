from django.contrib.auth.models import User
from django.db import models


class CreatedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Comment(CreatedModel):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Коммент'
        verbose_name_plural = 'Комменты'

    def __str__(self):
        return self.name
