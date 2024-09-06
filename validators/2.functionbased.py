# You can use any of Django's existing validators, or your own custom validators
# Function Based
# A validator may be any callable that raises a serializers.ValidationError on failure
def even_number(value):
    if value % 2 != 0:
        raise serializers.ValidationError("This field must be an even number.")

# Field-level validation, you can specify custom field-level validation
# By adding the .validate<field_name> methods to your Serializer subclass
