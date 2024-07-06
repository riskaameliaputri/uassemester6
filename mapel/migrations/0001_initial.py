# Generated by Django 5.0.4 on 2024-07-06 02:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
        ('dosen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MataPelajaran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('kode', models.CharField(max_length=20)),
                ('deskripsi', models.TextField()),
                ('dosen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dosen.dosen')),
                ('mahasiswa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.mahasiswa')),
            ],
        ),
    ]
