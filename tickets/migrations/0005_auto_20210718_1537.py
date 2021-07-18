# Generated by Django 3.2.3 on 2021-07-18 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_alter_ticket_date_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date_sent', models.DateTimeField(blank=True, verbose_name='Date Sent')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.ticket')),
            ],
        ),
        migrations.DeleteModel(
            name='FeedbackRequest',
        ),
    ]
