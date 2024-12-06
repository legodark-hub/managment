# Generated by Django 5.1.3 on 2024-12-04 19:46

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='invitation_code',
            field=models.UUIDField(default=uuid.uuid4, editable=False, null=True),
        ),
    ]
