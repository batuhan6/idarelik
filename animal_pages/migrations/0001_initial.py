# Generated by Django 3.2.16 on 2022-10-20 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_name', models.CharField(max_length=50, verbose_name='name')),
                ('descriptions', models.TextField(blank=True, default='Heyy are you ready to have a new awesome friend.', max_length=1000, null=True, verbose_name='descriptions')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]