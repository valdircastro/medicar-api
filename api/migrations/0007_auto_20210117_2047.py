# Generated by Django 3.1.5 on 2021-01-17 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210116_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='especialidade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.especialidade'),
        ),
    ]
