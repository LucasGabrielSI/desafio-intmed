from django.contrib import admin
from .models import Processor, Motherboard, MemoryRAM, VideoBoard


class ProcessorAdmin(admin.ModelAdmin):
    list_display = ['product', 'brand', ]
    search_fields = ['brand']


admin.site.register(Processor, ProcessorAdmin)


class MotherboardAdmin(admin.ModelAdmin):
    list_display = ['product', 'supported_processor', 'quantity_slots_ram', 'total_memory_ram_supported',
                    'integrated_video', ]
    search_fields = ['product']


admin.site.register(Motherboard, MotherboardAdmin)


class MemoryRamAdmin(admin.ModelAdmin):
    list_display = ['product', 'available_sizes', ]
    search_fields = ['product']


admin.site.register(MemoryRAM, MemoryRamAdmin)


class VideoBoardAdmin(admin.ModelAdmin):
    list_display = ['product', ]
    search_fields = ['product']


admin.site.register(VideoBoard, VideoBoardAdmin)
