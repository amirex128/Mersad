from django.urls import path, include

from rule_app.views import index_rule, create_rule

urlpatterns = [
    path('', index_rule),
    path('create', create_rule),
]
