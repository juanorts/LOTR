# Generated by Django 4.2.6 on 2023-10-31 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pelicula",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=100)),
                ("anyo", models.IntegerField()),
                ("director", models.CharField(max_length=50)),
                ("duracion", models.IntegerField()),
                ("genero", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Raza",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Personaje",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50)),
                ("genero", models.CharField(max_length=20)),
                ("colorOjos", models.CharField(max_length=15)),
                ("colorPelo", models.CharField(max_length=15)),
                ("estatura", models.IntegerField()),
                ("imagen", models.ImageField(upload_to="img/")),
                ("pelicula", models.ManyToManyField(to="appLOTR.pelicula")),
                (
                    "raza",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="appLOTR.raza"
                    ),
                ),
            ],
        ),
    ]
