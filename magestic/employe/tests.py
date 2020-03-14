from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from faker import Faker

from .models import Employe

import datetime
from io import BytesIO
# Create your tests here.
class TestModelEmploye(TestCase):
    """
        Test creation model and store database
    """
    def setUp(self):
        """
            Initialise data model
        """
        photo = SimpleUploadedFile('profile.png', b'\x47', content_type='image/png')
        e1 = Employe.objects.create(
            first_name = 'Harouna',
            last_name = 'Diallo',
            birthday = datetime.date(1996, 2, 5),
            fonction = 'Directeur',
            photo = photo
        )

    def test_model_employe(self):
        """
            Test model, database storage
        """
        employee = Employe.objects.all()
        self.assertEquals(1, employee.count())
        self.assertEquals('Harouna', employee[0].first_name)
        self.assertEquals('Diallo', employee[0].last_name)

class TestListEmployeProfileEndpoint(TestCase):
    """
        Test List Employe and Profile andpoint
    """
    def setUp(self):
        """
            Initialise data
        """
        self.fake = Faker()
        self.fake.random.seed(5467)

        photo = SimpleUploadedFile('profile.png', b'\x47', content_type='image/png')
        for _ in range(10):
            Employe.objects.create(
                first_name = self.fake.first_name(),
                last_name = self.fake.last_name(),
                birthday = datetime.date(1996, 2, 5),
                fonction = self.fake.job(),
                photo = photo
            )
        Employe.objects.create(
            first_name = 'Oumar',
            last_name = 'Diop',
            birthday = datetime.date(1991, 8, 5),
            fonction = 'DevOps',
            photo = photo
        )

    def test_list_employe_route(self):
        """
            Test list employe
        """
        url = reverse('employe_app:list-employe')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(response.context['employes']), 11) #15employe store

    def test_profile_route(self):
        """
            Test profile data
        """
        bad_url = reverse('employe_app:profile', kwargs={'id_employe': 999999})
        good_url = reverse('employe_app:profile', kwargs={'id_employe': 11})
        #bad url profile
        response = self.client.get(bad_url)
        self.assertEquals(response.status_code, 404)
        # Good url profile
        response = self.client.get(good_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['employe'].first_name, 'Oumar')
        self.assertEquals(response.context['employe'].last_name, 'Diop')

    def test_create_profile_route(self):
        """
            Test create profile endpoint
        """
        url = reverse('employe_app:create-employe')
        #bad url
        respons_not_allow = self.client.get(url)
        self.assertEquals(respons_not_allow.status_code, 405)
        #good url
        img = BytesIO(b'myphotodata')
        img.name = 'photo_khalifa.jpg'
        response = self.client.post(url,  {
            'first_name': 'Khalifa', 'last_name':'Diop',
            'function': 'Journaliste',
            'birthday': datetime.date(1992, 8, 5),
            'photo': img,
        }, format='json')
        self.assertEquals(response.status_code, 201)
