# Generated by Django 4.2.6 on 2023-11-06 11:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("appLOTR", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="pelicula",
            name="imagen",
            field=models.ImageField(default="img/default.jpg", upload_to="img/"),
        ),
        migrations.AddField(
            model_name="raza",
            name="actitud",
            field=models.CharField(default="null", max_length=20),
        ),
        migrations.AddField(
            model_name="raza",
            name="aspecto",
            field=models.CharField(default="null", max_length=20),
        ),
        migrations.AddField(
            model_name="raza",
            name="imagen",
            field=models.ImageField(default="img/default.jpg", upload_to="img/"),
        ),
        migrations.AddField(
            model_name="raza",
            name="longevidad",
            field=models.CharField(default="null", max_length=20),
        ),
        migrations.AddField(
            model_name="raza",
            name="tamnyo",
            field=models.CharField(default="null", max_length=20),
        ),
        migrations.AlterField(
            model_name="personaje",
            name="imagen",
            field=models.ImageField(default="img/default.jpg", upload_to="img/"),
        ),
        migrations.AlterField(
            model_name="raza",
            name="nombre",
            field=models.CharField(default="null", max_length=20),
        ),
    ]
