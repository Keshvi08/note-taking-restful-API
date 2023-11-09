from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    title=models.CharField(max_length=200)
    text=models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
 
  