from webbrowser import get
from django.db import models
from prognosis_generator import get_Prognosis
# Create your models here.
 
class PrognosisManager(models.Manager):
    def create_prognosis(self, zz, prognosis_text):
        prognose = self.create(zodiac_sign = zz, prognosis_text = get_Prognosis())
 
        return prognose
 
class Prognosis(models.Model):
    zodiac_sign = models.CharField(max_length=50)
    prognosis_text = models.TextField()
    created_at = models.DateField(auto_now= True)
 
    def __str__(self):
        return self.zodiac_sign + ' : ' + self.prognosis_text[0:50]
 
    objects = PrognosisManager()

# if Prognosis.objects.all().count() == 0:
#     aries = Prognosis.objects.create_prognosis("Овен", get_Prognosis())
#     taurus = Prognosis.objects.create_prognosis("Телец", get_Prognosis())
#     gemini = Prognosis.objects.create_prognosis("Близнецы", get_Prognosis())
#     cancer = Prognosis.objects.create_prognosis("Рак", get_Prognosis())
#     leo = Prognosis.objects.create_prognosis("Лев", get_Prognosis())
#     virgo = Prognosis.objects.create_prognosis("Дева", get_Prognosis())
#     libra = Prognosis.objects.create_prognosis("Весы", get_Prognosis())
#     scorpio = Prognosis.objects.create_prognosis("Скорпион", get_Prognosis())
#     sagittarius = Prognosis.objects.create_prognosis("Стрелец", get_Prognosis())
#     capicorn = Prognosis.objects.create_prognosis("Козерог", get_Prognosis())
#     aquarius = Prognosis.objects.create_prognosis("Водолей", get_Prognosis())
#     pisces = Prognosis.objects.create_prognosis("Рыбы", get_Prognosis())

aries = Prognosis.objects.create_prognosis("Овен", get_Prognosis())
taurus = Prognosis.objects.create_prognosis("Телец", get_Prognosis())
gemini = Prognosis.objects.create_prognosis("Близнецы", get_Prognosis())
cancer = Prognosis.objects.create_prognosis("Рак", get_Prognosis())
leo = Prognosis.objects.create_prognosis("Лев", get_Prognosis())
virgo = Prognosis.objects.create_prognosis("Дева", get_Prognosis())
libra = Prognosis.objects.create_prognosis("Весы", get_Prognosis())
scorpio = Prognosis.objects.create_prognosis("Скорпион", get_Prognosis())
sagittarius = Prognosis.objects.create_prognosis("Стрелец", get_Prognosis())
capicorn = Prognosis.objects.create_prognosis("Козерог", get_Prognosis())
aquarius = Prognosis.objects.create_prognosis("Водолей", get_Prognosis())
pisces = Prognosis.objects.create_prognosis("Рыбы", get_Prognosis())
