from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from borrowing.models import BorrowRecord
from borrowing.serializers import BorrowRecordSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from book.permissions import IsMember
# Create your views here.


# class BorrowRecordViewSet(ModelViewSet):
#     queryset = BorrowRecord.objects.all()
#     serializer_class = BorrowRecordSerializer

#     def get_permissions(self):
#         if self.request.method in ['GET']:
#             return [IsAuthenticated()]
#         return [IsAuthenticated(), IsAdminUser()]

class BorrowRecordViewSet(ModelViewSet):
    serializer_class = BorrowRecordSerializer
    permission_classes = [IsAuthenticated, IsMember]

    def get_queryset(self):
        return BorrowRecord.objects.filter(member=self.request.user.member)
