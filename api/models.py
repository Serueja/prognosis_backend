from django.db import models
from prognosis_generator import get_Prognosis
# Create your models here.

class PrognosisManager(models.Manager):
    def create_prognosis(self, zz, text, created):
        prognose = self.create(zodiac_sign = zz, prognosis_text = text, created_at = created)

        return prognose

class Prognosis(models.Model):
    zodiac_sign = models.CharField(max_length=50)
    prognosis_text = models.TextField()
    created_at = models.DateField(auto_now= True)

    def __str__(self):
        return self.zodiac_sign + ' : ' + self.prognosis_text[0:50]
    
    objects = PrognosisManager()
