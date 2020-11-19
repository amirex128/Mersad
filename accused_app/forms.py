from django import forms
from django.core.validators import RegexValidator, MaxLengthValidator


class AccusedForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control text-right mb-3 '}),
        label='نام',
        error_messages={
            'required': 'نام متهم الزامی میباشد',
            'max_length': 'نام متهم نباید بیشتر از 70 کارکتر باشد'
        },
        max_length=70
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control text-right mb-3 '}),
        label='نام خانوادگی',
        error_messages={
            'required': 'نام خانوادگی متهم الزامی میباشد',
            'max_length': 'نام خانوادگی متهم نباید بیشتر از 70 کارکتر باشد'
        },
        max_length=70
    )
    nation_code = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control text-right mb-3 '}),
        required=False,
        label='کد ملی',
        error_messages={
            'invalid': 'کد ملی وارد شده صحیح نمیباشد'
        },
        validators=[
            MaxLengthValidator(11, 'کد ملی وارد شده بیشتر از حد مجاز است')
        ]
    )
    phone = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control text-right mb-3 '}),
        required=False,
        label='شماره تماس',
        error_messages={
            'invalid': 'شماره تماس وارد شده صحیح نمیباشد'
        },
        validators=[
            RegexValidator(r'^09[0-9]{9}/$', 'شماره تماس وارد شده معتبر نمیباشد')
        ]
    )
    image = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'form-file-input text-right '}),
        required=False,
        label='تصویر متهم'
    )
    birthday = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control text-right mb-3 '}),
        required=False,
        label='تاریخ تولد',
        error_messages={
            'invalid': 'تاریخ تولد صحیح نمیباشد'
        }
    )
    father_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control text-right mb-3 '}),
        required=False,
        label='نام پدر',
        error_messages={
            'required': 'نام متهم الزامی میباشد',
            'max_length': 'نام متهم نباید بیشتر از 70 کارکتر باشد'
        },
        max_length=70
    )
    birth_city = forms.ChoiceField(
        widget=forms.TextInput(attrs={'class': 'form-control text-right mb-3 '}),
        required=False,
        label='محل تولد',
        error_messages={
            'required': 'نام متهم الزامی میباشد',
            'max_length': 'نام متهم نباید بیشتر از 70 کارکتر باشد'
        }
    )
    address = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control text-right mb-3 '}),
        required=False,
        label='آدرس'
    )
    arrest_at = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'class': 'form-control text-right mb-3 '}),
        required=False,
        label='ساعت دستگیری',
        error_messages={
            'invalid': 'تاریخ دستگیری صحیح نمیباشد'
        }
    )
