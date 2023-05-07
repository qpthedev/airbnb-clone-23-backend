# Generated by Django 4.1.7 on 2023-04-09 05:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("experiences", "0002_experience_category_alter_perk_detail_and_more"),
        ("rooms", "0004_room_category"),
        ("wishlists", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wishlist",
            name="experiences",
            field=models.ManyToManyField(blank=True, to="experiences.experience"),
        ),
        migrations.AlterField(
            model_name="wishlist",
            name="rooms",
            field=models.ManyToManyField(blank=True, to="rooms.room"),
        ),
    ]