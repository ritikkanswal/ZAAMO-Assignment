from rest_framework import serializers
from .models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
 class Meta:
  model = Restaurant
  fields = ['id','name', 'res_type', 'description','hours']



# class RestaurantSerializer(serializers.Serializer):
#     name=serializers.CharField(max_length=100)
#     age=serializers.IntegerField()
#     city=serializers.CharField(max_length=100)
