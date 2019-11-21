from .models import CompletePC
from rest_framework.serializers import ModelSerializer
from products.serializers import MotherboardSerializer, MemoryRAMSerializer, ProcessorSerializer, VideoBoardSerializer


class CompletePcSerializer(ModelSerializer):
    processor = ProcessorSerializer
    memory_ram = MemoryRAMSerializer
    video_board = VideoBoardSerializer
    motherboard = MotherboardSerializer

    class Meta:
        model = CompletePC
        fields = ['id', 'processor', 'memory_ram', 'video_board', 'motherboard']
