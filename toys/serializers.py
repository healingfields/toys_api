from rest_framework import serializers
from .models import Toy

class ToySerializer(serializers.Serializer):
  pk = serializers.IntegerField(read_only=True)
  name = serializers.CharField(max_length=100)
  description = serializers.CharField(max_length=250)
  release_date = serializers.DateTimeField()
  toy_category = serializers.CharField()
  was_home = serializers.BooleanField(required=False)

  def create(self, validated_data):
    return Toy.objects.create(**validated_data)

  def update(self, instance, validated_data):
    instance.name = validated_data.get('name', instance.name)
    instance.description = validated_data.get('description', instance.description)
    instance.release_date = validated_data.get('release_date', instance.release_date),
    instance.toy_categroy = validated_data.get('toy_category', instance.toy_category)
    instance.was_home = validated_data.get('was_home', instance.was_home)
    instance.save()
    return instance