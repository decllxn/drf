# The .is_valid() method takes an optional raise_excpetion flag that will causeit to raise a serializers.ValidationError exception if there are validation errors
# These exceptions are automatically dealt with by the defaulted exception handler that REST framework


# Return a 400 response if the data was invalid
serializer.is_valid(raise_exception=True)

