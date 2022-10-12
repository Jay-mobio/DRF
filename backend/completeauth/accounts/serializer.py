from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['email' , 'password','is_varified']
        
    # def create(self , validated_data):
    #     user = User.objects.create(email = validated_data['email'])
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user