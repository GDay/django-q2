# Generated by Django 4.1.5 on 2023-03-07 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("django_q", "0016_schedule_intended_date_kwarg"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="cluster",
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="ormq",
            name="key",
            field=models.CharField(
                help_text="Name of the target cluster", max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="ormq",
            name="lock",
            field=models.DateTimeField(
                help_text="Prevent any cluster from pulling until", null=True
            ),
        ),
        migrations.AlterField(
            model_name="schedule",
            name="cluster",
            field=models.CharField(
                blank=True,
                default=None,
                help_text="Name of the target cluster (Empty for any active cluster)",
                max_length=100,
                null=True,
            ),
        ),
    ]
