from django.urls import path
from django.views.generic import TemplateView

from member_app.views import save_member

app_name = 'member_app'
urlpatterns = [
    path('', TemplateView.as_view(template_name='member_app/index.html'), name='index'),
    path('create/save', save_member, name='do_save'),
    path('create', TemplateView.as_view(template_name='member_app/create.html'), name='create'),
    path('update/save', save_member, name='do_update'),
    path('update', TemplateView.as_view(template_name='member_app/update.html'), name='update'),
]
