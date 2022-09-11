from urllib import request
from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView

from .models import Plan
from .serializers import PlanSerializer


class PlanList(ListAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class PlanCreate(CreateAPIView):
    queryset = Plan.objects.all()
    # print(request)
    serializer_class = PlanSerializer


class PlanDelete(DestroyAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    lookup_field = 'id'
