# Generated by Django 2.2.6 on 2021-01-27 10:43

from django.db import migrations, models
import tools.Utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BInpatientInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('in_time', models.IntegerField(blank=True, null=True)),
                ('department', models.CharField(blank=True, max_length=40, null=True)),
                ('inpatient_area', models.CharField(blank=True, max_length=20, null=True)),
                ('bed_number', models.CharField(blank=True, max_length=20, null=True)),
                ('inpatient_number', models.CharField(blank=True, max_length=20, null=True)),
                ('in_date', models.DateField(blank=True, null=True)),
                ('out_date', models.DateField(blank=True, null=True)),
                ('out_record', models.FileField(upload_to=tools.Utils.get_out_record_direct)),
                ('progress_note', models.FileField(upload_to=tools.Utils.get_progress_note_direct)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'b_inpatient_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BInpatientMedicalAdvice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('medical_name', models.CharField(blank=True, max_length=40, null=True)),
                ('dose_num', models.FloatField(blank=True, null=True)),
                ('dose_unit', models.CharField(blank=True, max_length=10, null=True)),
                ('group', models.CharField(blank=True, max_length=10, null=True)),
                ('drug_type', models.CharField(blank=True, max_length=20, null=True)),
                ('type', models.IntegerField(blank=True, null=True)),
                ('usage_way', models.CharField(blank=True, max_length=20, null=True)),
                ('start_doctor', models.CharField(blank=True, max_length=20, null=True)),
                ('start_nurse', models.CharField(blank=True, max_length=20, null=True)),
                ('end_doctor', models.CharField(blank=True, max_length=20, null=True)),
                ('end_nurse', models.CharField(blank=True, max_length=20, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'b_inpatient_medical_advice',
                'managed': False,
            },
        ),
    ]
