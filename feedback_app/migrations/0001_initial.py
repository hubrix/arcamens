# Generated by Django 2.1.7 on 2019-05-09 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ECreateFeedback',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core_app.Event')),
                ('data', models.CharField(max_length=256, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='e_create_feedback1', to='core_app.Event')),
            ],
            options={
                'abstract': False,
            },
            bases=('core_app.event',),
        ),
    ]
