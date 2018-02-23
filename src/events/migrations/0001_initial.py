# Generated by Django 2.0.2 on 2018-02-17 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('basic', '0002_language'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=191, null=True)),
                ('description', models.TextField(null=True)),
                ('location', models.CharField(max_length=191, null=True)),
                ('location_coordinates', models.CharField(max_length=191, null=True)),
                ('ip_address', models.CharField(max_length=30, null=True)),
                ('user_agent', models.CharField(max_length=191, null=True)),
                ('start_timestamp', models.DateTimeField()),
                ('end_timestamp', models.DateTimeField(null=True)),
                ('recurring', models.BooleanField(default=False)),
                ('full_day_event', models.BooleanField(default=False)),
                ('banner', models.CharField(max_length=191, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='basic.Channel')),
                ('parent_event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
