# Generated by Django 2.1.5 on 2019-03-03 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('queued', 'queued'), ('processing', 'processing'), ('ready', 'ready'), ('error', 'error')], default='queued', max_length=14)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('received_t', models.DateTimeField(auto_now_add=True)),
                ('start_t', models.DateTimeField(null=True)),
                ('end_t', models.DateTimeField(null=True)),
            ],
        ),
    ]