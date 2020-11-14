from django.db import models


# Create your models here.

class Member(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    nation_code = models.IntegerField( unique=True)
    responsibility = models.CharField(max_length=500, null=True)
    type_team = models.CharField(max_length=500, null=True)
    birthday = models.DateField(null=True)
    father_name = models.CharField(max_length=500, null=True)
    city = models.CharField(max_length=500, default='مشهد', null=True)
    phone = models.IntegerField(unique=True)
    subscription_type = models.CharField(max_length=10, choices=[('n', 'normal'), ('a', 'active')], default='normal')
    province_corp = models.CharField(max_length=500, default='سپاه امام رضا')
    area = models.CharField(max_length=500, default='یاسر')
    realm = models.CharField(max_length=500, default='حوزه یک')
    base = models.CharField(max_length=500, null=True)
    equipment = models.CharField(max_length=500, default='تونفا')
    serial_equipment = models.CharField(max_length=500, default='1')

    def __str__(self):
        return self.first_name+' '+self.last_name




