from celery import shared_task

from airflows.services import set_currency



@shared_task(bind=True)
def auto_set_currencies(self):
    set_currency()
