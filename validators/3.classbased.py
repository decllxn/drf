# To write a class-based validator, use the __call__ method. CLass-based
# Validators are useful as they allow you to parameterize and reuse behavior

# Example

class MultipleOf:
    def __init__(self, base):
        self.base = base

    def __call__(self, value):
        if value % self.base != 0:
            message = 'This field must be a multiple of %d.' % self.base
            raise serializers.ValidationError(message)