from rest_framework import serializers
from library.models import Author, Book, Genre


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.__str__', read_only=True)
    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Book
        # fields = '__all__'
        fields = ('title', 'author', 'genres')
