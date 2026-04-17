from  rest_framework.decorators import api_view
from http import HTTPMethod, HTTPStatus

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Game, Genre
from .serializers import GameSerializer, GenreSerializer, UserSerializer


# from rest_framework import generics, permissions
# from rest_framework.authtoken.models import Token
# from django.contrib.auth import authenticate

# Create your views here.

@api_view(http_method_names=[HTTPMethod.GET, HTTPMethod.POST])
def games_list(request: Request) -> Response:
    if request.method == HTTPMethod.GET:
        return get_games()
    
    return create_games(request)


# @api_view(http_method_names=[HTTPMethod.GET, HTTPMethod.POST])
# def genres_list(request: Request) -> Response:
#     if request.method == HTTPMethod.GET:
#         return get_genres()
    
#     return create_genres(request)


def get_games() -> Response:
    return Response(
        GameSerializer(Game.objects.all(), many=True).data, status=HTTPStatus.OK
    )

def create_games(request: Request) -> Response:
    serializer = GameSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=HTTPStatus.CREATED)
    
    return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)


# def get_genres() -> Response:
#     return Response(
#         GenreSerializer(Genre.objects.all(), many=True).data, status=HTTPStatus.OK
#     )

# def create_genres(request: Request) -> Response:
#     serializer = GenreSerializer(data=request.data)

#     if serializer.is_valid:
#         serializer.save()
#         return Response(serializer.data, status=HTTPStatus.CREATED)
    
#     return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)


class genres_list(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data, status=HTTPStatus.OK)
    

    def post(self, request):
        serializer = GenreSerializer(data=request.data)

        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=HTTPStatus.CREATED)
        
        return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)
    

# class UserRegistrationView(generics.CreateAPIView):
#     serializer_class = UserSerializer
#     permission_classes = [permissions.AllowAny]

# class UserLoginView(APIView):
#     def post(self, request):
#         user = authenticate(username=request.data['username'], password=request.data['password'])
#         if user:
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({'token': token.key})
#         else: 
#             return Response({'error': 'Invalid Credentials'}, status=401)