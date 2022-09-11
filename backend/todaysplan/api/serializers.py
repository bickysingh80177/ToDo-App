from rest_framework import serializers
from api.models import Plan


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'item']
        # fields = "__all__"
