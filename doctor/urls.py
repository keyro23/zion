from django.urls import path
from .views import HomeTemplateView, AppointmentTemplateView, ManageAppointmentTemplateView, home
from .import views

urlpatterns = [
    path("HomeTemplateView", HomeTemplateView.as_view(), name="home"),
    path("make-an-appointment/", AppointmentTemplateView.as_view(), name="appointment"),
    path("manage-appointments", ManageAppointmentTemplateView.as_view(), name="manage"),
    path("blog/", views.blog, name="blog"),
    path("", views.home, name="zion"),
]
