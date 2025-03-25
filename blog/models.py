from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    SECTION_CHOICES = [
        ('linux', 'Linux'),
        ('windows', 'Windows'),
        ('macos', 'macOS'),
    ]
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', blank=True, null=True)  # Requiere Pillow
    section = models.CharField(max_length=20, choices=SECTION_CHOICES)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title