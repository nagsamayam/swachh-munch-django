import factory
from faker import Faker
from django.contrib.auth import get_user_model
from profiles.models import Profile
from basic.models import Channel


User = get_user_model()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)

    username = factory.Sequence(lambda n: 'username_{}'.format(n))
    email = factory.LazyAttribute(
        lambda obj: f'{obj.username}@example.com')
    password = factory.PostGenerationMethodCall('set_password', 'secret')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory, profile=None)
    location = factory.Iterator([
        'UNI Building, Millers Tank Bund Road, Vasanth Nagar, Bangalore - 560001',
        'New thippasandra, Market Road, Bangalore'
        'KR puram railway station, Bangalore',

    ])
    location_coordinates = factory.Iterator([
        '12.990954,77.597066',
        '12.973007,77.647256',
        '13.000556,77.675389'
    ])
    ip_address = Faker().ipv4()
    user_agent = Faker().user_agent()
    channel = factory.Iterator(Channel.objects.all())