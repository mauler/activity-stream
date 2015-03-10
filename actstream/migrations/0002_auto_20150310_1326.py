# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('actstream', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='action',
            name='action_object_content_type',
        ),
        migrations.RemoveField(
            model_name='action',
            name='action_object_object_id',
        ),
        migrations.AlterField(
            model_name='action',
            name='actor',
            field=models.ForeignKey(related_name='actor_actions', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
