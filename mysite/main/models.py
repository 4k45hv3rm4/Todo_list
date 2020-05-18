from django.db import models
from django.contrib.auth.models import User




class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    task = models.CharField(max_length=100)
    complete = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.task
