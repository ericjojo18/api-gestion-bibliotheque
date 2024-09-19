from rest_framework import serializers
from users.models import UserModel
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["first_name", "last_name","username", "email","password","librarian"]
        extra_kwargs = {'password':{'write_only': True}}

    def create(self, validated_data):
            user = UserModel.objects.create(
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                email=validated_data['email'],
                username=validated_data['username'],
                password=validated_data['password'],
                librarian=validated_data['librarian']
            )
            user.set_password(validated_data['password'])
            user.save()
            return user