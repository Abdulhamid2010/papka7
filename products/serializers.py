from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "email", "website", "github_link", "telegram_username", "password"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            website=validated_data.get("website", ""),
            github_link=validated_data.get("github_link", ""),
            telegram_username=validated_data.get("telegram_username", ""),
        )
        return user