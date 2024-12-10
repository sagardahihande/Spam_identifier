from rest_framework import serializers
from .models import User, Contact, SpamMarking

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'phone_number', 'email']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class SpamSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpamMarking
        fields = '__all__'
