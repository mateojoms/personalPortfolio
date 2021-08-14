from django.urls import path
from . import views
urlpatterns = [
    path('',views.HomeTemplateView.as_view(),name='home.html'),
    path('testmonial/',views.testmonial.as_view(),name = 'testmonials.html')
]