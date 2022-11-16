from django.urls import path
from .views import indexPageView, calculatorView, liftTypeView, bodyTypeView, crudTableView


urlpatterns = [
    path('', indexPageView, name='index'),
    path('calculator/', calculatorView, name='calculator'),
    path('liftType/', liftTypeView, name='liftType'),
    path('bodyType/', bodyTypeView, name='bodyType'),
    path('crudTable/', crudTableView, name='crudTable'),
]