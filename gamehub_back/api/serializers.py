from rest_framework import serializers
from .models import Genre, Game #, Manager

class GameSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Game
        fields = "__all__"

    
class GenreSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Genre
        fields = "__all__"

# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta: 
#         model = Manager
#         fields = "__all__"