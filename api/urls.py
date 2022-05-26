from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.getRoutes, name = "routes"),
    path('prognosis/', views.getPrognosis, name = "prognosis"),
    path('prognosis/<str:pk>/', views.getOnePrognosis, name = "prognosis"),
]