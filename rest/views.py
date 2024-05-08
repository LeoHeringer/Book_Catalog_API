from catalog.rest.models import Book
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from core.models import *

@api_view(['POST'])
def create_book(request):
    
    name = request.data.get("name")
    author = request.data.get("author")
    launch = request.data.get("launch")
    edition = request.data.get("edition")
    type =  request.data.get("typ")
    gender =  request.data.get("gender")
    publisher = request.data.get("publisher")
    year_edition = request.data.get("year")
    edition_number = request.data.get("edition_number")
    
    if not name:
        return Response({"message": "name invalid"}, status=status.http_400_BAd_REQUEST)
    
    if not author:
        return Response({"message": "name invalid"}, status=status.http_400_BAd_REQUEST)
    
    if not launch:
        return Response({"message": "name invalid"}, status=status.http_400_BAd_REQUEST)

    if not edition:
        return Response({"message": "name invalid"}, status=status.http_400_BAd_REQUEST)

    if not type:
        return Response({"message": "name invalid"}, status=status.http_400_BAd_REQUEST)

    if not gender:
        return Response({"message": "name invalid"}, status=status.http_400_BAd_REQUEST)

    if not publisher:
        return Response({"message": "name invalid"}, status=status.http_400_BAd_REQUEST)

    if not year_edition:
        return Response({"message": "name invalid"}, status=status.http_400_BAd_REQUEST)

    if not edition_number:
        return Response({"message": "name invalid"}, status=status.http_400_BAd_REQUEST)
    
    if Book.objects.filter(name=name, author=author):
        return Response({"message":"exists"}, status=status.HTTP_400_BAD_REQUEST)
    
    if name and author:
        Book.objects.create(name=name, author=author)
        return Response({"message":"create"}, status=status.HTTP_200_OK)
    
    return Response({"message":"invalid"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_book(request):

    book_name = request.query_params.get('name')

    book = Book.objects.filter(name=book_name)
    
    if not book.exists():
        return Response({"message":"book does not exist"}, status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_200_OK)