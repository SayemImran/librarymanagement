from rest_framework import serializers
from borrowing.models import BorrowRecord
from book.models import Book
from member.models import Member
from book.serializers import BookSerializer
from member.serializers import MemberSerializer


class BorrowRecordSerializer(serializers.ModelSerializer):
    book_detail = BookSerializer(source='book', read_only=True)
    member_detail = MemberSerializer(source='member', read_only=True)

    book = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(),
        write_only=True
    )
    member = serializers.PrimaryKeyRelatedField(
        queryset=Member.objects.all(),
        write_only=True
    )

    class Meta:
        model = BorrowRecord
        fields = ['id','book','member','book_detail','member_detail','borrow_date','return_date','is_returned']
