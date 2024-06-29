from django.urls import path

from web import views



urlpatterns=[

    path("UserRegister/",views.UserRegistration_view.as_view(),name="ureg"),

    path("UserLogin/",views.UserLogin_view.as_view(),name="ulog"),

]