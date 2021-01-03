from rest_framework import serializers
from books.models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:

        model = Book
        fields = ('title', 'subtitle', 'author', 'isbn') # to add custom fields  
