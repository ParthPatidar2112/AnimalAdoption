# Generated by Django 4.1.5 on 2023-12-03 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_application_applicant_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='pet_appllication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_name', models.TextField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=122, null=True)),
                ('phonenumber', models.IntegerField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('desc', models.TextField(blank=True, max_length=122, null=True)),
                ('status', models.CharField(default='1', max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='application',
        ),
    ]
