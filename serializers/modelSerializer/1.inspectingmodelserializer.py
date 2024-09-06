# Serialize  classes generate helpful verbose string reps
# Allow us to fully inspect the state of their fields
# Helpful in working with model serializers

# Specifying which fields to include
# I fyou only want a subset of the default fields to be used in a model
# serializer, you can do so using fields or exclude options
# fields = ('field1', 'field2', 'field3')

# Example
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'account_name', 'users', 'created_at']

# You can also set the fields attribute to a special value '__all__' indicates that all the fields in the model should be used
# fields = '__all__'
# You can also set the exclude attribute to a list of fields to be excluded from the serializer
# exclude = ['field1', 'field2', 'field3']