from django.urls import path, include

# from accused_app.views import create_accused, update_accused, AccusedList
from accused_app.views import AccusedList

app_name = 'accused'
urlpatterns = [
    path('list', AccusedList.as_view()),
    # path('create', create_accused, name='create'),
    # path('update/<int:accused_id>', update_accused),
]
