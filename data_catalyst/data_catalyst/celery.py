from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set default Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "data_catalyst.settings")

# create Celery app
app = Celery("data_catalyst")

# load settings from Django settings.py with CELERY_ prefix
app.config_from_object("django.conf:settings", namespace="CELERY")

# auto-discover tasks from installed apps
app.autodiscover_tasks()
