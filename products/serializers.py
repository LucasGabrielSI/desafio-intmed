from rest_framework.serializers import ModelSerializer
from products.models import MemoryRAM, Motherboard, Processor, VideoBoard


class ProcessorSerializer(ModelSerializer):
    class Meta:
        model = Processor
        fields = ['product', 'brand', ]


class MotherboardSerializer(ModelSerializer):
    class Meta:
        model = Motherboard
        fields = ['product', 'supported_processor', 'quantity_slots_ram', 'total_memory_ram_supported',
                  'integrated_video']


class MemoryRAMSerializer(ModelSerializer):
    class Meta:
        model = MemoryRAM
        fields = ['product', 'available_sizes', ]


class VideoBoardSerializer(ModelSerializer):
    class Meta:
        model = VideoBoard
        fields = ['product', ]
