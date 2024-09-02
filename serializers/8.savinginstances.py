# Saving instances
# If we want to be able to return complete object instances based on validated data we need to implemen  one or both of the 
# .create()
# .update() methods. For example


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length =200)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        return Comment(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validate_data.get('email', instance.email)
        instance.content = validate_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        return instance

# If your object instances correspond to Django models you'll also want to ensure that these methods save the object to the database
# For example, if Comment was a django model, the methods might look like this


def create(self, validated_data):
        return Comment.objects.create(**validated_data)

def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance
