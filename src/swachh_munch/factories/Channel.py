import factory
from faker import Faker
from basic.models import Channel


class ChannelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Channel

    title = factory.Iterator(['Website', 'ICMYC Android', 'ICMYC IOS', 'Swachhata IOS', 'Swachhata Android'])
    type = factory.Iterator(['Web', 'Android', 'IOS', 'IOS', 'Android'])
    platform = factory.Iterator(['I Change My City', 'Swachhata'])
