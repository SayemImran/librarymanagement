from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from book.models import Book, Author
from borrowing.models import BorrowRecord
from django.utils import timezone
from book.serializers import AuthorSerializer,BookSerializer
from book.permissions import IsMember
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get_permissions(self):
        if self.request.method in ['GET']:
            return [IsAuthenticated()]
        return [IsAuthenticated(), IsAdminUser()]
    @swagger_auto_schema(operation_summary="Add a new author (Admin only)")
    def create(self, request, *args, **kwargs):
        """Only Libraian can add update and delete authors"""
        return super().create(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary="Update an existing author (Admin only)")
    def update(self, request, *args, **kwargs):
        """Only Libraian can add update and delete authors"""
        return super().update(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary="Delete an author (Admin only)")
    def destroy(self, request, *args, **kwargs):
        """Only Libraian can add update and delete authors"""
        return super().destroy(request, *args, **kwargs)


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        elif self.action in ['borrow', 'return_book']:
            return [IsAuthenticated(), IsMember()]
        return [IsAuthenticated()]
    @swagger_auto_schema(operation_summary="Borrow a book (Members only)")
    @action(detail=True, methods=['post'], url_path='borrow')
    def borrow(self, request, pk=None):
        book = self.get_object()
        member = request.user.member

        if not book.available_status:
            return Response({"detail": "This book is already borrowed."}, status=status.HTTP_400_BAD_REQUEST)

        BorrowRecord.objects.create(book=book, member=member)
        book.available_status = False
        book.save()

        return Response({"detail": "Book borrowed successfully."}, status=status.HTTP_200_OK)
    @swagger_auto_schema(operation_summary="Return a borrowed book (Members only)")
    @action(detail=True, methods=['post'], url_path='return')
    def return_book(self, request, pk=None):
        book = self.get_object()
        member = request.user.member

        record = BorrowRecord.objects.filter(book=book, member=member, is_returned=False).first()

        if not record:
            return Response({"detail": "No active borrow record found for this book."}, status=status.HTTP_400_BAD_REQUEST)

        record.is_returned = True
        record.return_date = timezone.now().date()
        record.save()

        book.available_status = True
        book.save()

        return Response({"detail": "Book returned successfully."}, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(operation_summary="Add a new book (Admin only)")
    def create(self, request, *args, **kwargs):
        """Only authenticated users can add update and delete books"""
        return super().create(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary="Update an existing book (Admin only)")
    def update(self, request, *args, **kwargs):
        """Only authenticated users can add update and delete books"""
        return super().update(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary="Delete a book (Admin only)")
    def destroy(self, request, *args, **kwargs):
        """Only authenticated users can add update and delete books"""
        return super().destroy(request, *args, **kwargs)