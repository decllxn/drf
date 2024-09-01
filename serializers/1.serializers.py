# Serializers allo complexx datat types such as querysets and model instances to be converted to native python datatypes
# Python datatypes can then be easily rendered into JSON, XML or other content types
# Serializers also provide deserialization, allowing parsed data to be converted back into complex types
# Serializer class - Control output of our responses
# ModelSerializer - Provides a useful shortcut fro creating serializers that deal with model instances


# DECLARING SERIALIZERS
# Starting with an object first

from datetime import datetime

class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

comment = Comment(email='munene.declan1@gmail.com', content='foo bar')

# We'll now declare a serializer that we can use to serialize and deserialize data that corresponds to Comment
# Objects

from rest_framework import serializers

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()