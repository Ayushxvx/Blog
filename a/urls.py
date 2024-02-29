from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("register",views.register,name="register"),
    path("login",views.login_user,name="login"),
    path("addpost",views.addpost,name="addpost"),
    path("posts/<str:id>",views.specific,name="specific"),
    path("logout",views.logout_user),
    path("<str:string>",views.anything)
]