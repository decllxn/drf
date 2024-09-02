# Now when deserializing data, we can call the .save() to return an object instance, based on the validated data

comment = serializer.save()

# Calling the .save() will either create a new instance or update an existing instance, depending on if an existing instance was passed when instantiating the serializer class

# .save will create a new instance
serializer = CommentSerializer(data=data)

# .save() will update the existing 'comment' instance
serializer = COmmentSerializer(comment, data=data)


# PASSING ADDITIONAL ATTRIBUTES TO .save()
# Sometimes you'll want your view code to be able to inject additional data at the point of saving the instance.
# THis addittional data might include information like the current user, the current time, or anything els that is not part of the request data
# You can do so by including additional keyword arguments when calling .save()

serializer.save(owner=request.user)

# Any additional keyword arguments will be included in the validated_data argument when .create() or .update() are called
