# While the default serializers provided by drf are powerful and flexible
# There are cases where you need to customize the serialization and deserialization process,
# To meet the specific requirements of the API

# Drf allows us to extend and customize serializers in a variety of ways
# Adding custom fields - You can add custom fields that are not directly mapped to model fields
# Ovverdiding default behavior - You can ovveride the default serialization and deserialization logic to implement custom lgic
# Handling complex data structures - Serializers can handle nested datastructures, such as one-to-many or many-to-many relationships

# Example
from rest_framework import serializers
from .models import BlogPost, Comment

class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.CharFIeld(source='author.username', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'content', 'author', 'author_name', 'created_at']
# Custom field author_name field displays the username of the comment's author
