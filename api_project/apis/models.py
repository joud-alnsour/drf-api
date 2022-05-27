from django.db import models
from django.contrib.auth import get_user_model


class Api(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    purshaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE , null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title