from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .serializers import BookSerializer


from .models import Book

@api_view(['POST'])
def create_book(request):
    name = request.data.get('name')
    author = request.data.get('author')
    
        
    if Book.objects.filter(name=name, author=author).exists():
        return Response({"message": "Book already exists"}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_book(request):

    book_name = request.query_params.get('name')

    book = Book.objects.filter(name=book_name)
    
    if not book.exists():
        return Response({"message":"book does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = BookSerializer(book.first())

    return Response(serializer.data, status=status.HTTP_200_OK)