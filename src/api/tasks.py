import logging

from core.services import get_emails_for_notify
from core.celery import app

logger = logging.getLogger(__name__)


@app.task(queue="default")
def get_emails():
    emails_to_notify = get_emails_for_notify()
    logger.info(f"emails {len(emails_to_notify)} need notify")
