from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.PlanList.as_view(), name='listitem'),
    path('create/', views.PlanCreate.as_view(), name='createitem'),
    path('delete/<int:id>', views.PlanDelete.as_view(), name='deleteitem'),
]
