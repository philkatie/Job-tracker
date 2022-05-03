# Generated by Django 4.0.4 on 2022-05-03 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_remove_document_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='user',
        ),
        migrations.RemoveField(
            model_name='job',
            name='documents',
        ),
        migrations.AddField(
            model_name='document',
            name='job',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.job'),
            preserve_default=False,
        ),
    ]
