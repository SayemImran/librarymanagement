from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from member.serializers import MemberSerializer
from member.models import Member
# Create your views here.

class MemberViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer