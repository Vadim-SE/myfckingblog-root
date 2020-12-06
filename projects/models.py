from django.db import models

# Create your models here.
class Project(models.Model):
	project_image = models.ImageField(upload_to='project_images/')
	project_text = models.CharField(max_length=300)
