from django.db import models


class Processor(models.Model):
    INTEL = 'INTEL'
    AMD = 'AMD'

    TYPE_BRAND = [
        (INTEL, 'INTEL'),
        (AMD, 'AMD'),
    ]

    product = models.CharField(verbose_name='Produto', max_length=255)
    brand = models.CharField(verbose_name='Marca', choices=TYPE_BRAND, max_length=255)

    def __str__(self):
        return self.product

    class Meta:
        verbose_name = 'Processador'
        verbose_name_plural = 'Processadores'


class Motherboard(models.Model):
    INTEL = 'INTEL'
    AMD = 'AMD'
    INTEL_AMD = 'INTEL E AMD'

    SUPPORTED_PROCESSOR = [
        (INTEL, 'INTEL'),
        (AMD, 'AMD'),
        (INTEL_AMD, 'INTEL E AMD')
    ]

    TOTAL_MEMORY_SUPPORTED = [
        ('OPCAO1', 'Até 16 GB'),
        ('OPCAO2', 'Até 64 GB'),
    ]

    product = models.CharField(verbose_name='Produto', max_length=255)
    supported_processor = models.CharField(verbose_name='Processador suportado', choices=SUPPORTED_PROCESSOR,
                                           max_length=255)
    quantity_slots_ram = models.IntegerField(verbose_name='Quantidade de slots de RAM')
    total_memory_ram_supported = models.CharField(verbose_name='Total de memórias RAM suportado',
                                                  choices=TOTAL_MEMORY_SUPPORTED, max_length=10)
    integrated_video = models.BooleanField(verbose_name='Vídeo Integrado', default=True)

    def __str__(self):
        return self.product

    class Meta:
        verbose_name = 'Placa Mãe'
        verbose_name_plural = 'Placas Mãe'


class MemoryRAM(models.Model):
    AVAILABLE_SIZES = [
        ('OPCAO1', '4 GB'),
        ('OPCAO2', '8 GB'),
        ('OPCAO3', '16 GB'),
        ('OPCAO4', '32 GB'),
        ('OPCAO5', '64 GB'),
    ]

    product = models.CharField(verbose_name='Produto', max_length=255)
    available_sizes = models.CharField(verbose_name='Tamanhos disponíveis', choices=AVAILABLE_SIZES, max_length=20)

    def __str__(self):
        return self.product

    class Meta:
        verbose_name = 'Memória RAM'
        verbose_name_plural = 'Memória RAM'


class VideoBoard(models.Model):
    product = models.CharField(verbose_name='Produto', max_length=255)

    def __str__(self):
        return self.product

    class Meta:
        verbose_name = 'Placa de vídeo'
        verbose_name_plural = 'Placas de vídeo'
