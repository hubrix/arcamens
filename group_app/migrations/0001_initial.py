# Generated by Django 2.1.7 on 2019-05-09 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core_app', '0002_auto_20190509_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='EBindGroupUser',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core_app.Event')),
                ('status', models.CharField(choices=[('0', 'Admin'), ('1', 'Member'), ('2', 'Guest')], max_length=6)),
            ],
            options={
                'abstract': False,
            },
            bases=('core_app.event',),
        ),
        migrations.CreateModel(
            name='ECreateGroup',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core_app.Event')),
            ],
            options={
                'abstract': False,
            },
            bases=('core_app.event',),
        ),
        migrations.CreateModel(
            name='EDeleteGroup',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core_app.Event')),
                ('group_name', models.CharField(max_length=250, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('core_app.event',),
        ),
        migrations.CreateModel(
            name='EPastePost',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core_app.Event')),
            ],
            options={
                'abstract': False,
            },
            bases=('core_app.event',),
        ),
        migrations.CreateModel(
            name='EUnbindGroupUser',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core_app.Event')),
            ],
            options={
                'abstract': False,
            },
            bases=('core_app.event',),
        ),
        migrations.CreateModel(
            name='EUpdateGroup',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core_app.Event')),
            ],
            options={
                'abstract': False,
            },
            bases=('core_app.event',),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open', models.BooleanField(blank=True, default=False, help_text='Contributors can also post over.')),
                ('public', models.BooleanField(blank=True, default=False, help_text='Visible to all organization members.')),
                ('name', models.CharField(help_text='Example: Bugs', max_length=250, null=True, verbose_name='Name')),
                ('description', models.CharField(blank=True, default='', help_text='Example: /projectname/', max_length=626, verbose_name='Description')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('node', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='group', to='core_app.Node')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='core_app.Organization')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owned_groups', to='core_app.User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupPin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='group_app.Group')),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core_app.Organization')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Groupship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('0', 'Admin'), ('1', 'Member'), ('2', 'Guest')], default='2', max_length=6)),
                ('binder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='binder_groupship', to='core_app.User')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='group_app.Group')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_groupship', to='core_app.User')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='groups', through='group_app.Groupship', to='core_app.User'),
        ),
        migrations.AddField(
            model_name='eupdategroup',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='e_update_group', to='group_app.Group'),
        ),
        migrations.AddField(
            model_name='eunbindgroupuser',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='e_unbind_group_user', to='group_app.Group'),
        ),
        migrations.AddField(
            model_name='eunbindgroupuser',
            name='peer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core_app.User'),
        ),
        migrations.AddField(
            model_name='epastepost',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='e_paste_post0', to='group_app.Group'),
        ),
    ]
