import requests
from users.models import User
from orders.models import CompletePC
from products.models import Processor, MemoryRAM, VideoBoard, Motherboard

from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class CompletePcTests(APITestCase):
    def setUp(self):
        User.objects.create(name='test', email='test@test.com', )
        Processor.objects.create(product='Processador Intel Core i5', brand='INTEL')
        MemoryRAM.objects.create(product='Hiper X', available_sizes='4 GB')
        VideoBoard.objects.create(product='Placa de Video Gigabyte Geforce GTX 1060 6GB')
        Motherboard.objects.create(product="Placa Mãe ASRock Fatal", supported_processor='INTEL',
                                   quantity_slots_ram=2, total_memory_ram_supported="Até 16 GB",
                                   integrated_video=True)

    def test_create_completePC(self):
        """
        Ensure we can create a new completePC object.
        """
        user = User.objects.get(name='test', email='test@test.com', )

        self.client = APIClient()
        self.client.force_authenticate(user=user)

        url = 'https://apisilvertec.pythonanywhere.com/api/orders/mount_computer/'
        data = {'id_processor': 1,
                'id_memory_ram': [1, 1],
                'id_motherboard': 1,
                'id_video_board': 1
                }
        response = self.client.post(url, data=data)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CompletePC.objects.count(), 1)

    def test_return_all_completePC(self):
        """
        Ensure we can return all instances of model CompletePC.
        """
        user = User.objects.get(name='test', email='test@test.com', )

        self.client = APIClient()
        self.client.force_authenticate(user=user)

        response = self.client.get('https://apisilvertec.pythonanywhere.com/api/orders/list_complete_pcs/')
        assert response.status_code == 200
