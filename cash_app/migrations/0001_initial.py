# Generated by Django 2.1.7 on 2019-05-09 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('paybills', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Period',
            fields=[
                ('basicitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='paybills.BasicItem')),
                ('price', models.IntegerField(default=0)),
                ('max_users', models.IntegerField(help_text='Max users until the expiration.', null=True)),
                ('expiration', models.DateField(help_text='Example: year-month-day', null=True)),
                ('total', models.FloatField(default=0)),
                ('paid', models.BooleanField(default=False)),
            ],
            bases=('paybills.basicitem',),
        ),
    ]
