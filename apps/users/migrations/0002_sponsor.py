# Generated by Django 4.2.1 on 2023-05-19 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sponsor_type', models.CharField(choices=[('PHYSICAL', 'Physical person'), ('LEGAL', 'Legal entity')], default='LEGAL', max_length=15)),
                ('status', models.CharField(choices=[('NEW', 'New'), ('MODERATION', 'In moderation'), ('CANCELED', 'Canceled'), ('CONFIRMED', 'Confirmed')], default='MODERATION', max_length=12)),
                ('summa', models.BigIntegerField(help_text='Sponsorship amount')),
                ('organization', models.CharField(blank=True, help_text='Organization name', max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sponsor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Sponsors',
                'ordering': ['-user__date_joined'],
            },
        ),
    ]
