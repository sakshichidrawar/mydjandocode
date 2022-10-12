from django.contrib import admin
from django.urls import path,include
from.import views
urlpatterns = [
path('stu1/', views.student_view),
]
