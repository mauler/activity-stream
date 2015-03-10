# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0001_initial'),
        ('subs', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('verb', models.CharField(max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
                ('action_object_object_id', models.CharField(max_length=255, null=True, blank=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('public', models.BooleanField(default=True)),
                ('data', jsonfield.fields.JSONField(null=True, blank=True)),
                ('action_object_content_type', models.ForeignKey(related_name='action_object', blank=True, to='contenttypes.ContentType', null=True)),
                ('actor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('target', models.ForeignKey(to='subs.Post')),
            ],
            options={
                'ordering': ('-timestamp',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actor_only', models.BooleanField(default=True, verbose_name=b'Only follow actions where the object is the target.')),
                ('started', models.DateTimeField(default=django.utils.timezone.now)),
                ('follow_object', models.ForeignKey(related_name='followed_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together=set([('user', 'follow_object')]),
        ),
    ]
