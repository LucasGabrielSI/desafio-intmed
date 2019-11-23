from .models import CompletePC
from .serializers import CompletePcSerializer
from products.models import Processor, Motherboard, MemoryRAM, VideoBoard

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny


class CompletePcViewSet(ModelViewSet):
    queryset = CompletePC.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = [CompletePcSerializer]

    @action(methods=['POST'], detail=False, permission_classes=[IsAuthenticated, ])
    def mount_computer(self, request):
        """
        service to receive id of components for mount the computer.
        Being an invalid request, the server reject or the request returning errors made by the customer are returned,
        if not, Being a valid request, the server creates the request by storing it in the database of the store, and
        returns your customer information.
        """
        try:
            user = request.user
            id_processor = str(request.data['id_processor'])
            id_memory_ram = list(request.data['id_memory_ram'])
            id_motherboard = str(request.data['id_motherboard'])
            id_video_board = str(request.data['id_video_board'])
        except ValueError as exc:
            return Response({'success': False, 'status': status.HTTP_400_BAD_REQUEST, 'error': str(exc)})

        if len(id_processor) > 1:
            return Response({'success': False, 'status': status.HTTP_400_BAD_REQUEST,
                             'message': 'Opss, Você só deve selecionar um processador!'})
        if len(id_motherboard) > 1:
            return Response({'success': False, 'status': status.HTTP_400_BAD_REQUEST,
                             'message': 'Opss, Você só deve selecionar uma placa mãe!'})
        if len(id_video_board) > 1:
            return Response({'success': False, 'status': status.HTTP_400_BAD_REQUEST,
                             'message': 'Opss, Você só deve selecionar uma placa de vídeo!'})
        if len(id_memory_ram) is 0:
            return Response({'success': False, 'status': status.HTTP_400_BAD_REQUEST,
                             'message': 'Opss, Você deve selecionar ao menos uma memória RAM!'})

        try:
            processor = Processor.objects.get(id=id_processor)
        except Processor.DoesNotExist as exc:
            return Response({'success': False, 'status': status.HTTP_400_BAD_REQUEST,
                             'error': str(exc)})
        try:
            motherboard = Motherboard.objects.get(id=id_motherboard)
        except Motherboard.DoesNotExist as exc:
            return Response({'success': False, 'status': status.HTTP_400_BAD_REQUEST,
                             'error': str(exc)})

        if not((processor.brand is motherboard.supported_processor) or (
           (motherboard.supported_processor == motherboard.INTEL_AMD)
           and (processor.brand == 'INTEL' or processor.brand == 'AMD'))):
            return Response({'success': False, 'status': status.HTTP_400_BAD_REQUEST,
                             'message': 'Opss, A placa mãe selecionada não suporta o processador selecionado'})

        if len(id_memory_ram) > motherboard.quantity_slots_ram:
            return Response({'success': False, 'status': status.HTTP_400_BAD_REQUEST,
                             'message': 'Opss, A quantitade de memórias ram selecionas superam a quantidade suportada '
                                        'pela placa mãe'})

        if len(id_memory_ram) > 1:
            total = 0
            for memory_ram in id_memory_ram:
                memory_ram = MemoryRAM.objects.get(id=memory_ram)
                total += int(memory_ram.available_sizes)
            if total > int(motherboard.total_memory_ram_supported):
                return Response({'success': False, 'status': status.HTTP_400_BAD_REQUEST,
                                 'message': 'Opss, A quantitade total de armazenamento em GB não deve superar o total '
                                            'de memória RAM suportada pela placa mãe!'})
        if not motherboard.integrated_video:
            if len(id_video_board) is 0:
                return Response({'success': False, 'status': status.HTTP_400_BAD_REQUEST,
                                 'message': 'Opss, Sua placa mãe não possui vídeo integrado, você deve selecionar uma '
                                            'placa de vídeo'})
            else:
                try:
                    video_board = VideoBoard.objects.get(id=id_video_board)
                except VideoBoard.DoesNotExist as exc:
                    return Response({'success': False, 'status': status.HTTP_400_BAD_REQUEST,
                                     'error': str(exc)})
                list_memory = []
                for memory_ram in id_memory_ram:
                    memory_ram = MemoryRAM.objects.get(id=memory_ram)
                    list_memory.append(memory_ram)
                complete_pc = CompletePC.objects.create(name_client=user,
                                                        processor=processor,
                                                        video_board=video_board,
                                                        motherboard=motherboard)
                complete_pc.Memory_ram.set(list_memory)
                serializer = CompletePcSerializer(complete_pc, many=False)
                complete_pc.save()
                return Response({'success': True, 'status': status.HTTP_201_CREATED,
                                 'message': 'Computador montado com sucesso!', 'data': serializer.data})
        else:
            if len(id_video_board) is 0:
                list_memory = []
                for memory_ram in id_memory_ram:
                    memory_ram = MemoryRAM.objects.get(id=memory_ram)
                    list_memory.append(memory_ram)
                complete_pc = CompletePC.objects.create(name_client=user,
                                                        processor=processor,
                                                        motherboard=motherboard)
                complete_pc.Memory_ram.set(list_memory)
                serializer = CompletePcSerializer(complete_pc, many=False)
                complete_pc.save()
                return Response({'success': True, 'status': status.HTTP_201_CREATED,
                                 'message': 'Computador montado com sucesso!', 'data': serializer.data})
            else:
                try:
                    video_board = VideoBoard.objects.get(id=id_video_board)
                except VideoBoard.DoesNotExist as exc:
                    return Response({'success': False, 'status': status.HTTP_400_BAD_REQUEST,
                                     'error': str(exc)})
                list_memory = []
                for memory_ram in id_memory_ram:
                    memory_ram = MemoryRAM.objects.get(id=memory_ram)
                    list_memory.append(memory_ram)
                complete_pc = CompletePC.objects.create(name_client=user,
                                                        processor=processor,
                                                        video_board=video_board,
                                                        motherboard=motherboard)
                complete_pc.Memory_ram.set(list_memory)
                serializer = CompletePcSerializer(complete_pc, many=False)
                complete_pc.save()
                return Response({'success': True, 'status': status.HTTP_201_CREATED,
                                 'message': 'Computador montado com sucesso!', 'data': serializer.data})
