from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<url_id>/', views.short_url, name='short_url'),
]