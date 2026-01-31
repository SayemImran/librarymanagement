from rest_framework import serializers
from member.models import Member,CustomUser
from django.contrib.auth.models import User
from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer


class UserCreateSerializer(BaseUserCreateSerializer):
    membership_date = serializers.DateField(required=True)
    class Meta(BaseUserCreateSerializer.Meta):
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name','password','membership_date','phone_number','address']
    def create(self, validated_data):
        membership_date = validated_data.pop('membership_date')
        user = super().create(validated_data)
        Member.objects.create(user=user, membership_date=membership_date)
        return user

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name','membership_date','phone_number','address']


class MemberSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.get_full_name', read_only=True)
    email = serializers.EmailField(source='user.email')
    phone_number = serializers.CharField(source='user.phone_number')
    class Meta:
        model = Member
        fields = ['id','name','email','membership_date','phone_number']