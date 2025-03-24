# Generated by Django 5.0.6 on 2024-08-27 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_alter_user_is_active_alter_user_is_staff_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(help_text="Email", max_length=255, unique=True, verbose_name="email"),
        ),
        migrations.AlterField(
            model_name="user",
            name="passage_id",
            field=models.CharField(help_text="Passage ID", max_length=255, unique=True, verbose_name="passage_id"),
        ),
    ]
