from django.urls import path, include

from accused_app.views import index_accused, create_accused, update_accused, show_create_accused

app_name = 'accused'
urlpatterns = [
    path('', index_accused),
    path('create', show_create_accused),
    path('create', create_accused, name='create'),
    path('update/<int:accused_id>', update_accused),
]
