# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shorturl', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='item',
            new_name='new_url',
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='store',
            new_name='original_url',
        ),
    ]
