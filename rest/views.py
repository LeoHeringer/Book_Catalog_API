from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .serializers import BookSerializer


from .models import Book

@api_view(['POST'])
def create_book(request):
    book_data = request.data
    
    existing_book = Book.objects.filter(name=book_data.get('name'), author=book_data.get('author')).exists()
    
    if existing_book:
        return Response({"message": "Book already exists"}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = BookSerializer(data=book_data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_book(request):

    book_name = request.query_params.get('name')
    book = Book.objects.filter(name=book_name)
    
    if book:
        serializer = BookSerializer(book.first())
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response({"message": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_book(request):
    book = request.query_params.get('name')
    update_book = Book.objects.filter(name=book).first()
    
    if not update_book:
        return Response({"message":"Book not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = BookSerializer(update_book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Updated successfully"}, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['DELETE'])
def delete_book(request):
    book_id = request.query_params.get('id')
    delete_book = Book.objects.filter(id=book_id).first()
    
    if delete_book:
        delete_book.delete()
        return Response({"message": "Book successfully deleted"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Book not found"}, status=status.HTTP_400_BAD_REQUEST)