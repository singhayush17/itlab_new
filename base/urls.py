# urls for app

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

 
from . import views


urlpatterns=[

    path('login/',views.loginPage,name = "login"),
    path('payments/success',views.success,name = "success"),
    path('payments/',views.payments,name = "payments"),
    path('register/',views.registerPage,name = "register"),
    path('logout/',views.logoutUser,name = "logout"),
    path('',views.home,name="home"),
    path('room/<str:pk>/',views.room,name="room"),
    path('profile/<str:pk>/',views.userProfile,name="user-profile"),
    path('create-room/',views.createRoom,name="create-room"),
    path('update-room/<str:pk>',views.updateRoom,name="update-room"),
    path('delete-room/<str:pk>',views.deleteRoom,name="delete-room"),
    path('delete-message/<str:pk>',views.deleteMessage,name="delete-message"),
    path('update-user/',views.updateUser,name="update-user"),
    path('topics/',views.topicsPage,name="topics"),
    path('activity/',views.activityPage,name="activity"),
    path('about/',views.about,name="about"),
    path('adS/',views.adS,name="adS"),
    path('create_startup_profile/',views.create_startup_profile,name="create_startup_profile"),
    path('create-meeting/',views.createMeeting,name="create-meeting"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

] 