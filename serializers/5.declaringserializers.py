# Declaring Serializers
# Let's start by creating a simple object we can use for example purposes

from datetime import datetime

class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

comment = Comment(email='munene.declan1@gmail.com', content='foo bar')

# We'll declare a serializer that we can use to serialize and deserialize data
# that corresponds to comment objects

from rest_framework import serializers

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharFIeld(max_length=200)
    created = serializers.DateTimeField()


# Serializing objects
# We can now use CommentSerializer to serialize a comment, or a list of comments# Using the serializer class looks alot like using a Form class

serializer = CommentSerializer(comment)
serializer.data

# Output:
# {'email': 'leila@example.com', 'content': 'foo bar', 'created': '2016-01-27T15:17:10.375877'}


# At this point we have translated the model instance into Python native datatypes
# TO finalise the serialization process we render the data into json
