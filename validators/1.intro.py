# Serializers can also be used to validate incoming data before creatinh or updating
# Model instances
# You can define custom validation by overriding the validate method in our serializer
# Example
from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'author', 'created_at']

    def validate(self, data):
        if len(data['title']) < 5:
            raise serializers.ValidationError('Title must be at least 5 characters long')
        return data
# In the above example, the validate method checks if the title field in the incoming data is atleast
# 5 characters long. If not, it raises a validation error.