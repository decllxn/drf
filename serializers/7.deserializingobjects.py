# Deserialization is similar. First we parse a stream into Python native datatypes...

import io
from rest_framework.parsers import JSONParser

stream = io.BytesIO(json)
data = JSONParser().parse(stream)

# then we restore those native datatypes into a dictionary of validated data

serializer = CommentSerializer(data=data)
serializer.is_valid()

# True
serializer.validated_data
{'content': 'foo bar', 'email': 'leila@example.com', 'created': datetime.datetime(2012, 08, 22, 16, 20, 09, 822243)}
