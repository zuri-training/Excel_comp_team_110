# Generated by Django 4.0.6 on 2022-08-07 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('prefer not to say', 'PREFER NOT TO SAY'), ('female', 'FEMALE'), ('others', 'OTHERS'), ('male', 'MALE')], default='prefer not to say', max_length=20),
        ),
    ]
