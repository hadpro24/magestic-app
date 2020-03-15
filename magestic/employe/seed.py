import datetime
from faker import Faker
from .models import Employe
from django.core.files.uploadedfile import SimpleUploadedFile

fake = Faker(['fr_FR'])
fake.random.seed(500)

photo = SimpleUploadedFile('profile.png', b'\x47', content_type='image/png')
def lunch_seed():
    for _ in range(10):
        Employe.objects.create(
            first_name = fake.first_name(),
            last_name = fake.last_name(),
            birthday = fake.date_object(end_datetime=None),
            fonction = fake.job(),
            photo = photo
        )
