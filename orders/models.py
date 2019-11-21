import utils
from django.db import models
from django.contrib.auth.models import User
from products.models import Processor, Motherboard, MemoryRAM, VideoBoard


class CompletePC(models.Model):
    name_client = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Nome do cliente', max_length=255)
    processor = models.ForeignKey(to=Processor, on_delete=models.CASCADE, related_name='processor', )
    Memory_ram = models.ForeignKey(to=MemoryRAM, on_delete=models.CASCADE, related_name='memory_ram')
    video_board = models.ForeignKey(to=VideoBoard, on_delete=models.CASCADE, related_name='video_board')
    motherboard = models.ForeignKey(to=Motherboard, on_delete=models.CASCADE, related_name='motherboard')

    def __str__(self):
        return 'COMPUTADOR COMPLETO - CODÍGO: ' + utils.random_string()

    class Meta:
        verbose_name = 'Computador Completo'
        verbose_name_plural = 'Computadores Completos'
