from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ[ 'DJANGO_SETTINGS_MODULE' ] = "btc_usd_api.settings"

app = Celery('btc_usd_api')
app.conf.broker_transport_options = {"visibility_timeout": max_timeout_in_seconds}
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = 'redis://localhost:6379/0'
app.autodiscover_tasks()