# Generated by Django 2.2 on 2021-07-11 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_bpatientrtms'),
    ]

    operations = [
        migrations.CreateModel(
            name='RPatientBlood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_sample_id', models.CharField(blank=True, max_length=45, null=True)),
                ('blood_sampling_date', models.DateField(blank=True, null=True)),
                ('inspect_date', models.DateField(blank=True, null=True)),
                ('total_blood_number', models.IntegerField(blank=True, null=True)),
                ('plasma_number', models.IntegerField(blank=True, null=True)),
                ('hemocyte_number', models.IntegerField(blank=True, null=True)),
                ('extract_dna', models.FloatField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'r_patient_blood',
                'managed': False,
            },
        ),
    ]
