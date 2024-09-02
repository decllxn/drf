# When deserializing data, you always need to call is_valid() before attempting
# to access the validated data, or save an object instance.
# If any validation errors occur, the .errors property will contain a dictionary representing the resulting error messages

serializer = CommentSerializer(data={'email': 'foobar', 'content': 'baz'})
serializer.is_valid

# False
serializer.errors
# {'email': ['Enter a valid e-mail address.'], 'created': ['This field is required.']}

# Each Key in the dictionary will be the field name, and the values will be lists of stirngs of any error messages corresponding to that field
# non_field_errors - Key may also be presen, and will list any general validation errors
# non_field_errors - Key may be customized using the NON_FIELD_ERRORS_KEY Rest framework setting

# When deserializing a list of items, errors will be returned as a list of dictionaries representing each of the deserialized items

