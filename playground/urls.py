from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('hello/', views.HelloView.as_view(),name='hello-view')
]
