from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('admin/', admin.site.urls),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("profile", views.profile, name="profile"),
    path("editprofile", views.edit_profile, name="edit_profile"),
    path("userprofile/<int:user_id>", views.user_profile, name="user_profile"),
    path("compose", views.compose, name="compose"),
    path("message/<int:message_id>", views.message, name="message"),
    path("mailbox/<str:mailbox>", views.mailbox, name="mailbox"),
    path("messages", views.messages, name="messages"),
    path("match", views.match, name="match"),
    path("register", views.register, name="register")
]
