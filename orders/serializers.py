from .models import CompletePC

from rest_framework.serializers import ModelSerializer

from users.serializers import UserSerializer
from products.serializers import MotherboardSerializer, MemoryRAMSerializer, ProcessorSerializer, VideoBoardSerializer


class CompletePcSerializer(ModelSerializer):
    processor = ProcessorSerializer
    Memory_ram = MemoryRAMSerializer
    video_board = VideoBoardSerializer
    motherboard = MotherboardSerializer
    information_of_client = UserSerializer

    class Meta:
        model = CompletePC
        depth = 1
        fields = ['id', 'information_of_client', 'processor', 'Memory_ram', 'video_board', 'motherboard', 'create_at']
