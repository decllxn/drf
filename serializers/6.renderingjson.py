from rest_framework.renderers import JSONRenderer

json = JSONRenderer().render(serializer.data)

# Output
# b'{"email":"leila@example.com","content":"foo bar","created":"2016-01-27T15:17:10.375877"}'
