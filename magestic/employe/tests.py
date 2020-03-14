from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Employe

import datetime
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
