# Generated by Django 2.0.2 on 2018-02-17 11:44

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.CharField(max_length=50, null=True)),
                ('otp', models.CharField(max_length=191, null=True)),
                ('location', models.CharField(max_length=191, null=True)),
                ('location_coordinates', models.CharField(max_length=191, null=True)),
                ('ip_address', models.CharField(max_length=30, null=True)),
                ('user_agent', models.CharField(max_length=191, null=True)),
                ('apn_token', models.CharField(max_length=191, null=True)),
                ('gcm_token', models.CharField(max_length=191, null=True)),
                ('mac_address', models.CharField(max_length=191, null=True)),
                ('avatar', models.CharField(max_length=191, null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='basic.Channel')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'auth_profile',
            },
        ),
    ]