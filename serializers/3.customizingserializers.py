# Serializers can be customed in various ways to meet your specific requirements
# Some of the most common customization options include:
# Adding custom fields - You can add custom fields to your serializer that are not directly mapped to model fields
# Performing validations - Serializers can validate incoming data before creating or updating model instances
# Handling complex data structures - Serializers can handle nested data structures, such as one-to-many,
# many-to-many, and foreign key relationships
# Overriding default behavior -  You can override the default serialization and deserialization logic to implement custom logic
from rest_framework import serializers
from .models import MyModel

class MyModelSerializer(serializers.ModelSerializer):
    days_since_created = serializers.SerializerMethodField()

    class Meta:
        model = MyModel
        fields = ('id', 'name', 'description', 'created_at', 'days_since_created')

    def get_days_since_created(self, obj):
        from datetime import datetime, timezone
        return (datetime.now(timezone.utc) - obj.created_at).days
    
# In the above example, the days_since_created field is a custom field that calculates the number of days
# Since the model instance was created
