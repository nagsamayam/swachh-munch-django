import factory
from faker import Faker
from basic.models import Language


class LanguageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Language

    name = factory.Iterator(
        ['English', 'Telegu', 'Hindi', 'Tamil', 'Malayalam', 'Kannada'])
    code = factory.Iterator(['en', 'te', 'hi', 'ta', 'ml', 'kn'])
    label = factory.Iterator(
        ['English', 'తెలుగు', 'हिन्दी', 'தமிழ்', 'മലയാളം', 'ಕನ್ನಡ'])
