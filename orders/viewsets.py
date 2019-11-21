from .models import CompletePC
from products.models import Processor, Motherboard, MemoryRAM, VideoBoard
from .serializers import CompletePcSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny


class CompletePcViewSet(ModelViewSet):
    queryset = CompletePC.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = [CompletePcSerializer]

    @action(methods=['POST'], detail=False, permission_classes=[AllowAny, ])
    def mount_computer(self, request):
        """
        service to receive id of components for mount the computer.
        Being an invalid request, the server reject or the request returning errors made by the customer are returned,
        if not, Being a valid request, the server creates the request by storing it in the database of the store, and
        returns your customer information.
        """
        user = request.user
        processor_id = request.data['processor_id']
        memory_ram_id = request.data['memory_ram_id']
        motherboard_id = request.data['motherboard_id']
        video_board_id = request.data['video_board_id']

        processor = Processor.objects.get(id=processor_id)
        memory_ram = MemoryRAM.objects.get(id=memory_ram_id)
        video_board = VideoBoard.objects.get(id=video_board_id)
        motherboard = Motherboard.objects.get(id=motherboard_id)

        if len(processor_id) is 1:
            if len(motherboard_id) is 1:
                if processor.brand is motherboard.supported_processor:
                    if len(memory_ram_id) >= 1:
                        if len(memory_ram_id) is motherboard.quantity_slots_ram:
                            if memory_ram.available_sizes is motherboard.total_memory_ram_supported:
                                if len(video_board_id) is 1 and video_board.integrated_video:
                                    complete_pc = CompletePC.objects.create(name_client=user,
                                                                            processor=processor,
                                                                            memory_ram=memory_ram,
                                                                            video_board=video_board,
                                                                            motherboard=motherboard)
                                    complete_pc.save()
                                    return Response({'success': True, 'message': 'Pc montando com sucesso'})
                                elif len(video_board_id) is 1 and not video_board.integrated_video:
                                    complete_pc = CompletePC.objects.create(name_client=user,
                                                                            processor=processor,
                                                                            memory_ram=memory_ram,
                                                                            motherboard=motherboard)
                                    complete_pc.save()
                                    return Response({'success': True, 'message': 'Pc montando com sucesso'})
                                else:
                                    message1 = 'É possível selecionar apenas uma placa de vídeo para compor a máquina'
                            else:
                                message2 = ''
