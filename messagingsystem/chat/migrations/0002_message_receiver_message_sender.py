# Generated by Django 4.1.3 on 2023-07-18 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_users_delete_user'),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to='users.users'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to='users.users'),
            preserve_default=False,
        ),
    ]