# Generated by Django 5.1.1 on 2024-09-18 14:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('publication_date', models.DateField()),
                ('available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='BorrowingModel',
            fields=[
                ('bookmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='books.bookmodel')),
                ('borrowed_at', models.DateTimeField(auto_now_add=True)),
                ('return_at', models.DateTimeField(blank=True, null=True)),
                ('returned', models.BooleanField(default=False)),
            ],
            bases=('books.bookmodel',),
        ),
        migrations.CreateModel(
            name='ReservationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_at', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.bookmodel')),
            ],
        ),
    ]
