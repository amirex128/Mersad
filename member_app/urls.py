from django.urls import path, include

from member_app.views import create_member, index_member

urlpatterns = [
    path('', index_member),
    path('create', create_member),
]
