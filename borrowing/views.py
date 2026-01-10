from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from borrowing.models import BorrowRecord
from borrowing.serializers import BorrowRecordSerializer
# Create your views here.


class BorrowRecordViewSet(ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer