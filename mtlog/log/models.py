from django.db import models

# Create your models here.

class log_page(models.Model):
    log_title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    published_date = models.DateTimeField(auto_now_add=True)
    lastmodified_date = models.DateTimeField(auto_now_add=True)
    contents = models.TextField()

    
