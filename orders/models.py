import utils
import datetime

from django.db import models

from users.models import User
from products.models import Processor, Motherboard, MemoryRAM, VideoBoard


class CompletePC(models.Model):
    information_of_client = models.ForeignKey(to=User, default=None, on_delete=models.CASCADE, verbose_name='Cliente',)
    processor = models.ForeignKey(to=Processor, on_delete=models.CASCADE, related_name='processor', )
    Memory_ram = models.ManyToManyField(to=MemoryRAM, related_name='memory_ram')
    video_board = models.ForeignKey(to=VideoBoard, on_delete=models.CASCADE, related_name='video_board', null=True,
                                    blank=True)
    motherboard = models.ForeignKey(to=Motherboard, on_delete=models.CASCADE, related_name='motherboard',)
    create_at = models.DateTimeField(verbose_name='Data e hora da criação', default=datetime.datetime.now())

    def __str__(self):
        return 'COMPUTADOR COMPLETO - CODÍGO: ' + utils.random_string()

    class Meta:
        verbose_name = 'Computador Completo'
        verbose_name_plural = 'Computadores Completos'
