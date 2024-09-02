# In some cases the .create() or .update() method names may not be meaningful.For example, in a contact form we may not be creating new instances, but instead sending an email or other message

# In these cases you might instead choose to override .save() directly, as being more readable and meaningful

# For example
class ContactForm(serializers.Serializer):
    email = serializers.EmailField()
    message = serializers.CharField()

    def save(self):
        email = self.validated_data['email']
        message = self.validated_data['message']
        send_email(from=email, message=message)

# Note that in the case above we're now having to access the serializer .validated_data property directly
