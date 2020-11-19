from django.db import models


# Create your models here.

class Accused(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    nation_code = models.IntegerField(unique=True, null=True)
    phone = models.IntegerField(unique=True, null=True)
    image = models.ImageField(null=True)
    birthday = models.DateField(null=True)
    father_name = models.CharField(max_length=500, null=True)
    birth_city = models.CharField(max_length=500, null=True)
    address = models.CharField(max_length=1000, null=True)
    arrest_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = 'accuseds'

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Crime(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(null=True)
    address = models.CharField(max_length=1000, null=True)
    accused = models.ForeignKey(Accused, on_delete=models.CASCADE, related_name='crimes')

    class Meta:
        db_table = 'crimes'

    def __str__(self):
        return self.title
