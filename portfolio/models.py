from django.db import models
from django.db.models import Model

# Create your models here.;
class Portfolio(models.Model):
    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=500)
    image=models.ImageField(upload_to="portfolio/images")
    urls=models.URLField()
     
    def __str__(self):
        return self.name

class MainImage(models.Model):
    title=models.CharField(max_length=10)
    topimage=models.ImageField(upload_to="portfolio/images")

    def __str__(self):
        return self.title
