# Generated by Django 2.1.7 on 2019-05-09 14:33

from django.db import migrations, models
import django.db.models.deletion
import list_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('card_app', '0001_initial'),
        ('board_app', '0001_initial'),
        ('core_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ECopyList',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core_app.Event')),
                ('ancestor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='e_copy_list0', to='board_app.Board')),
            ],
            options={
                'abstract': False,
            },
            bases=('core_app.event',),
        ),
        migrations.CreateModel(
            name='ECreateList',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core_app.Event')),
                ('ancestor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='e_create_list0', to='board_app.Board')),
            ],
            options={
                'abstract': False,
            },
            bases=('core_app.event',),
        ),
        migrations.CreateModel(
            name='ECutList',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core_app.Event')),
                ('ancestor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='e_cut_list0', to='board_app.Board')),
            ],
            options={
                'abstract': False,
            },
            bases=('core_app.event',),
        ),
        migrations.CreateModel(
            name='EDeleteList',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core_app.Event')),
                ('child_name', models.CharField(blank=True, max_length=255, null=True)),
                ('ancestor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='e_delete_list0', to='board_app.Board')),
            ],
            options={
                'abstract': False,
            },
            bases=('core_app.event',),
        ),
        migrations.CreateModel(
            name='EPasteCard',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core_app.Event')),
            ],
            options={
                'abstract': False,
            },
            bases=('core_app.event',),
        ),
        migrations.CreateModel(
            name='EUpdateList',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core_app.Event')),
                ('ancestor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='e_update_list0', to='board_app.Board')),
            ],
            options={
                'abstract': False,
            },
            bases=('core_app.event',),
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True, verbose_name='Name')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('description', models.CharField(blank=True, default='', help_text='Example: Things to do.', max_length=626, verbose_name='Description')),
                ('ancestor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lists', to='board_app.Board')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core_app.User')),
            ],
            bases=(list_app.models.ListMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ListFilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pattern', models.CharField(blank=True, default='', max_length=255)),
                ('status', models.BooleanField(blank=True, default=False, help_text='Filter On/Off.')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='list_filter', to='board_app.Board')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_app.Organization')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='ListPin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='list_app.List')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_app.Organization')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_app.User')),
            ],
            bases=(list_app.models.ListPinMixin, models.Model),
        ),
        migrations.AddField(
            model_name='eupdatelist',
            name='child',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='e_update_list1', to='list_app.List'),
        ),
        migrations.AddField(
            model_name='epastecard',
            name='ancestor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='e_paste_card0', to='list_app.List'),
        ),
        migrations.AddField(
            model_name='epastecard',
            name='cards',
            field=models.ManyToManyField(related_name='e_paste_card1', to='card_app.Card'),
        ),
        migrations.AddField(
            model_name='ecutlist',
            name='child',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='e_cut_list1', to='list_app.List'),
        ),
        migrations.AddField(
            model_name='ecreatelist',
            name='child',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='e_create_list1', to='list_app.List'),
        ),
        migrations.AddField(
            model_name='ecopylist',
            name='child',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='e_copy_list1', to='list_app.List'),
        ),
        migrations.AlterUniqueTogether(
            name='listpin',
            unique_together={('user', 'organization', 'list')},
        ),
        migrations.AlterUniqueTogether(
            name='listfilter',
            unique_together={('user', 'organization', 'board')},
        ),
    ]
