from django.urls import path, include

from report_app.views import index_report, create_report

urlpatterns = [
    path('', index_report),
    path('create', create_report),
]
