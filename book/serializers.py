from rest_framework import serializers
from book.models import Book, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name','bio']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only = True)
    author_id = serializers.IntegerField()

    class Meta:
        model = Book
        fields = ['id','title','author','author_id','isbn','category','available_status' ]
        