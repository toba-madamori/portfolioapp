from django.db import models

# Create your models here.

class ResumeFile(models.Model):
    resume = models.FileField(upload_to='media')
    title = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title