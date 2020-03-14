from django.db import models

# Create your models here.
class Employe(models.Model):
    """
        Employe Model
    """
    first_name =  models.CharField(max_length=30)
    last_name  = models.CharField(max_length=30)
    birthday   = models.DateField()
    fonction   = models.CharField(max_length=100)
    photo      = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'
