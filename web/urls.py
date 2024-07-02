from django.urls import path

from web import views



urlpatterns=[

    path("home/",views.Home_view.as_view(),name="home"),

    path("UserRegister/",views.UserRegistration_view.as_view(),name="ureg"),

    path("UserLogin/",views.UserLogin_view.as_view(),name="ulog"),

    path("LogOut/",views.UserLogout_view.as_view(),name="Ulogout"),

    path("UpdateUser/<int:pk>/",views.UserProfileUpdate_view.as_view(),name="UpdateUser"),

    path("ChangeUserPassword/",views.ChangeUserPassword_view.as_view(),name="ChangeUserPassword"),

    path("UserProfileDelete/<int:pk>/",views.UserProfileDelete.as_view(),name="del"),

]