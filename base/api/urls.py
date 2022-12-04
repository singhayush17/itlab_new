from django.urls import path
from . import views
from .views import StartupAPIView
from django.urls import include, re_path

urlpatterns = [
    re_path('startups',StartupAPIView.as_view())
    # path('startups/', views.getStartups),
    # path('startups/<str:pk>/', views.getStartup),
]