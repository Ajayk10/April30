from django.urls import path,include
from April30 import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('I/', views.I, name = 'I'),
    path('II/', views.II, name = 'II'),
    path('III/', views.III, name = 'III'),
    path('IV/', views.IV, name = 'IV'),
    path('V/', views.V, name = 'V'),
    path('VI/', views.VI, name = 'VI'),
    path('VII/', views.VII, name = 'VII'),
    path('VIII/', views.VIII, name = 'VIII'),
    path('IX/', views.IX, name = 'IX'),
    path('X/', views.X, name = 'X'),
    path('record/', views.record, name = 'record'),
]
