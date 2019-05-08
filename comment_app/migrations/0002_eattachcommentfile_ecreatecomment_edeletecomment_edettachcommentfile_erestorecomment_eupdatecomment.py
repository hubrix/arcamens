# Generated by Django 2.1.7 on 2019-05-08 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core_app', '0001_initial'),
        ('comment_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EAttachCommentFile',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core_app.Event')),
            ],
            options={
                'abstract': False,
            },
            bases=('core_app.event',),
        ),
        migrations.CreateModel(
            name='ECreateComment',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core_app.Event')),
            ],
            options={
                'abstract': False,
            },
            bases=('core_app.event',),
        ),
        migrations.CreateModel(
            name='EDeleteComment',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core_app.Event')),
                ('comment', models.CharField(max_length=626, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('core_app.event',),
        ),
        migrations.CreateModel(
            name='EDettachCommentFile',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core_app.Event')),
                ('filename', models.CharField(max_length=626, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('core_app.event',),
        ),
        migrations.CreateModel(
            name='ERestoreComment',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core_app.Event')),
                ('event_html', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('core_app.event',),
        ),
        migrations.CreateModel(
            name='EUpdateComment',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core_app.Event')),
                ('comment_title', models.CharField(max_length=626, null=True, verbose_name='Label')),
                ('comment_html', models.TextField(blank=True, null=True)),
                ('comment_data', models.TextField(blank=True, default='', help_text='Markdown content.', verbose_name='Data')),
            ],
            options={
                'abstract': False,
            },
            bases=('core_app.event',),
        ),
    ]
