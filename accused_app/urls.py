from django.urls import path, include

from accused_app.views import index_accused, create_accused, update_accused

app_name = 'accused_app'
urlpatterns = [
    path('', index_accused),
    path('create', create_accused),
    path('update/<int:accused_id>', update_accused),
]
