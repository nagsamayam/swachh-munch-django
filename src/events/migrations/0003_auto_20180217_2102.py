# Generated by Django 2.0.2 on 2018-02-17 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20180217_2027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='parent_event_id',
        ),
        migrations.AddField(
            model_name='event',
            name='parent_event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='events.Event'),
        ),
    ]