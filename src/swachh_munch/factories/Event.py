from basic.models import Channel
from events.models import Event
import factory
from faker import Faker
from .User import UserFactory
from django.utils import timezone


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Event

    title = Faker().sentence()
    description = Faker().paragraph(15)
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
    start_timestamp = timezone.make_aware(Faker().future_datetime(end_date="+1d", tzinfo=None), timezone.get_current_timezone())
    owner = factory.SubFactory(UserFactory, profile=None)
    channel = factory.Iterator(Channel.objects.all())

