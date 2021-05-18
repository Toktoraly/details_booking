# Generated by Django 3.2 on 2021-05-15 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_alter_doctor_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='profes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.profes'),
        ),
    ]
