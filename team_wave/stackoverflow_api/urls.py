from django.urls import path,include
from .views import GetAll_Questions_View,Get_By_Query_View

urlpatterns = [
    path('getAll/',GetAll_Questions_View.as_view(),name='getAll'),
    path('getByQuery/',Get_By_Query_View.as_view(),name='getByQuery')
]
