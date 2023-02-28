from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "is_superuser",
            "password",
            "username",
            "email",
            "is_adm",
        ]
        read_only_fields = ["id", "is_superuser"]
        extra_kwargs = {
            "password": {"write_only": True},
            "is_adm": {
                "default": False,
            },
        }

    def create(self, validated_data: dict) -> User:
        if validated_data["is_adm"]:
            return User.objects.create_superuser(**validated_data)

        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance
