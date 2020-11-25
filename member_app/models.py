from django.db import models

# Create your models here.
from django.utils import timezone


class Member(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    nation_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=11)
    responsibility = models.CharField(max_length=500)
    father_name = models.CharField(max_length=500)
    birthday = models.DateField(null=True)
    city = models.CharField(max_length=500, choices=[('1', 'مشهد')],
                            default='1')
    type_team = models.CharField(max_length=500, choices=[('base', 'پایگاه'), ('support', 'پشتیبانی')],
                                 default='base')
    subscription_type = models.CharField(max_length=10, choices=[('normal', 'عادی'), ('active', 'فعال')],
                                         default='normal')
    province_corp = models.CharField(max_length=500, choices=[('1', 'سپاه امام رضا')], default='1')
    area = models.CharField(max_length=500, choices=[('1', 'یاسر')], default='1')
    realm = models.CharField(max_length=500, choices=[('1', 'حوزه یک')], default='1')
    base = models.CharField(max_length=500,
                            choices=[
                                ('1', 'چوپانی'),
                                ('2', 'ولایت'),
                                ('3', 'رزمندگان'),
                                ('4', 'صاحب الزمان'),
                                ('5', 'امام حسین'),
                            ]
                            , default='1')
    equipment = models.CharField(max_length=500,
                                 choices=[
                                     ('1', 'تونفا'),
                                     ('2', 'شکر / اففشانه'),
                                     ('3', 'کلاشینیکف'),
                                 ]
                                 , default='1')
    serial_equipment = models.CharField(max_length=500, default='1')
    register_at = models.DateField(auto_created=True, default=timezone.now)

    class Meta:
        db_table = 'members'

    def __str__(self):
        return self.first_name + ' ' + self.last_name
