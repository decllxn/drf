# Serializer Types
# ModelSerializer - Automates serializer creation based on a django model , including field definition and basic validation
# HyperLinkedModelSerializer - Extends ModelSerializer to include hyperlinks to related models
# Serializer - Provides a base class for creating custom serializers with more control over fields and validation


# Validation
# DRF serializers include built-in validation mechanisms to ensure data integrity
# You can define validation rules using various methods
# Field-level validation
# Object level validation
# Custom validation functions
# You can define custom validation rules by overriding the validate method in your serializer

from rest_framework import serializers
from .models import MyModel

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__' 

    def validate(self, data):
        if len(data['name']) < 5:
            raise serializers.ValidationError('Name must be at least 5 characters long')
        return data
    

# In the above example, the validate method checks if the namefield in the incoming data is atleast 5 characters long
# If the validation fails, a ValidationError is raised, which will be returned to the client in the response
