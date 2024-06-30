# apps/core/serializers.py

from rest_framework import serializers
from django.core.validators import MinLengthValidator
from django.utils import timezone
from apps.users.models import CustomUser  # Import CustomUser model from users app
from apps.core.models import Contact, AboutUs

class ContactSerializer(serializers.ModelSerializer):
    resolved_by = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    time_since_created = serializers.SerializerMethodField()
    time_since_updated = serializers.SerializerMethodField()

    class Meta:
        model = Contact
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'resolved_by', 'user']

    def get_resolved_by(self, obj):
        if obj.resolved_by:
            return {
                'id': obj.resolved_by.id,
                'name': obj.resolved_by.name,
                'surname': obj.resolved_by.surname,
                'email': obj.resolved_by.email,
            }
        return None

    def get_user(self, obj):
        if obj.user:
            return {
                'id': obj.user.id,
                'name': obj.user.name,
                'surname': obj.user.surname,
                'email': obj.user.email,
            }
        return None

    def get_time_since_created(self, obj):
        return timezone.now() - obj.created_at

    def get_time_since_updated(self, obj):
        return timezone.now() - obj.updated_at

class AboutUsSerializer(serializers.ModelSerializer):
    last_updated_by = serializers.SerializerMethodField()
    word_count = serializers.SerializerMethodField()

    class Meta:
        model = AboutUs
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'last_updated_by']
        extra_kwargs = {
            'content': {'validators': [MinLengthValidator(50)]}
        }

    def get_last_updated_by(self, obj):
        if obj.last_updated_by:
            return {
                'id': obj.last_updated_by.id,
                'name': obj.last_updated_by.name,
                'surname': obj.last_updated_by.surname,
                'email': obj.last_updated_by.email,
            }
        return None

    def get_word_count(self, obj):
        return len(obj.content.split())

    def validate_content(self, value):
        if len(value) < 50:
            raise serializers.ValidationError("Content must be at least 50 characters long.")
        return value
