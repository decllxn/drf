# Serializers manage data retrieval and filtering from the database
# Basic serializer
from rest_framework import serializers
from .models import MyModel

class MyModelSeriializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'  # or specify fields individually
        # fields = ['id', 'name', 'description', 'created_at']


# In the above example, MyModelSerializer is responsible for serializing and deserializin  instances
# Of MyModels
# The fields attribute specifies which model fields should be included in the serialized output
# The '__all__' value means all fields will be included
