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

    opcao1 = '16'
    opcao2 = '64'

    TOTAL_MEMORY_SUPPORTED = [
        (opcao1, 'Até 16 GB'),
        (opcao2, 'Até 64 GB'),
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
    opcao1 = '4'
    opcao2 = '8'
    opcao3 = '16'
    opcao4 = '32'
    opcao5 = '64'

    AVAILABLE_SIZES = [
        (opcao1, '4 GB'),
        (opcao2, '8 GB'),
        (opcao3, '16 GB'),
        (opcao4, '32 GB'),
        (opcao5, '64 GB'),
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
