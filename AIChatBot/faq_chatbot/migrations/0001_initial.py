# Generated by Django 4.1 on 2024-07-01 13:55

from django.db import migrations, models
import pgvector.django.indexes
import pgvector.django.vector
from pgvector.django import VectorExtension



class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        VectorExtension(),
        
        migrations.CreateModel(
            name='FAQs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('general', 'General Queries'), ('challenge', 'The Challenge'), ('funded', 'The Funded Account')], max_length=100)),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('embedding', pgvector.django.vector.VectorField(dimensions=1536)),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQs',
                'db_table': 'faqs',
            },
        ),
        migrations.AddIndex(
            model_name='faqs',
            index=pgvector.django.indexes.IvfflatIndex(fields=['embedding'], name='faqs_embeddi_7195fc_ivfflat'),
        ),
    ]