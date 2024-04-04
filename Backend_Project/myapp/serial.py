# myapp/serializers.py
from rest_framework import serializers
from .models import CustomUser, Paragraph

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'name', 'dob', 'created_at', 'modified_at']
        read_only_fields = ['created_at', 'modified_at']

class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ['id', 'text', 'created_at']
        read_only_fields = ['created_at']
