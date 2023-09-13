from django.db import models


class article(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=128)
    ref = models.CharField(max_length=128)
    desgn = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    qty = models.FloatField(default=0.0)
    
    class Meta:
        ordering = ['id']
        
    def __str__(self):
        return self.title