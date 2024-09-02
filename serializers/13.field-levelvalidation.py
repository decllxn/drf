# You can specify custom field-level validation by adding .validate_<field_name>
# Methods to your serializer subclass
# There are similar to the .clean<field_name> methods on Django forms

# Your validate_<field_name> methods should return the validated value or raise a 
# serializers.ValidationError
# Example

from rest_framework import serializers

class BlogPostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()

    def validate_title(self, value):
        if 'django' not in value.lower():
            raise serializers.ValidationError("Blog post is not about Django")
        return value
    
# The above title validator, checks if the blog post is about Django
# If not, it raises a ValidationError with a message
# NOTE: if your <field_name> is declared on your serializer with  the parameter required=False
# then this validation step will not take place if the field is not included
