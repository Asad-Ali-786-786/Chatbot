# Generated by Django 5.1.4 on 2024-12-28 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0002_chatmessage_delete_message'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ChatMessage',
        ),
    ]
