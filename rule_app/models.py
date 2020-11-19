from django.db import models


# Create your models here.
class Rule(models.Model):
    subject = models.CharField(max_length=500)
    day = models.CharField(max_length=500)
    started_at = models.CharField(max_length=500)
    hour_start = models.CharField(max_length=500)
    hour_end = models.CharField(max_length=500)
    equipment = models.CharField(max_length=500)
    serial_equipment = models.CharField(max_length=500)
    province_mission = models.CharField(max_length=500)
    city_mission = models.CharField(max_length=500)
    area_mission = models.CharField(max_length=500)
    realm_mission = models.CharField(max_length=500)
    base_mission = models.CharField(max_length=500)
    destination_mission = models.CharField(max_length=500)
    vehicle = models.CharField(max_length=500)
    vehicle_code = models.CharField(max_length=500)
    vehicle_driver = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'rules'
