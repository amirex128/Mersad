import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from accused_app.models import Accused, Crime


class CrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crime
        fields = '__all__'
        # ه دلیل این که وقتی تمامی داده ها را میفرستیم به سریالایز و میبیند فیلد accused وجود ندارد خطا میدهد برای
        # همین از الزامی بودن برمیداریم تا بتوان داده ها را ارسال کنیم
        extra_kwargs = {'accused': {'required': False}}


class AccusedSerializer(serializers.ModelSerializer):
    # در صورتی که این فیلد اضافه شود در خروجی جدول مرتبط رو هم برمیگردونه فقط باید نام این فیلد با اسم فیلد related_name
    # داخل مدل یکی باشد
    crimes = CrimeSerializer(many=True, read_only=True)
    crime = CrimeSerializer(write_only=True)

    class Meta:
        model = Accused
        fields = '__all__'

    # def validate_phone(self, value):
    #
    #     re_compile = re.compile('^09[0-9]{9}$')
    #     match = re_compile.match(str(value))
    #     if match:
    #         return value
    #     else:
    #         raise ValidationError('Your phone number is not valid')

    def create(self, validated_data):
        crimes = validated_data.pop('crime')
        accused = Accused.objects.create(**validated_data)
        Crime.objects.create(**crimes, accused=accused)
        return accused
