import os
from celery import Celery

# Configure Celery with broker and optional result backend
app = Celery(
    'tasks',
    broker=os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0"),
    backend=os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")
)

# Celery configuration
app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
    task_track_started=True,
    result_expires=3600,
)


@app.task(bind=True)
def add(self, x, y):
    """Add two numbers asynchronously."""
    return x + y
