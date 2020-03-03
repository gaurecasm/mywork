from django.db import models

# Create your models

class Book(models.Model):

    title        = models.CharField(blank=False, unique=True, max_length=40,)
    description  = models.TextField(blank=True, max_length=400,)
    price        = models.DecimalField(default=0, max_digits=3, decimal_places=2,)
    published    = models.DateField(blank=True, null=True, default=None,)
    is_published = models.BooleanField(default=False,)

    cover        = models.ImageField(upload_to='covers/', blank=True,)


    def  __str__(self):
        return self.title
        