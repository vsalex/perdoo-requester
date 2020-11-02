import json
import logging
import os
from json import JSONDecodeError

import requests
import django

from apscheduler.schedulers.blocking import BlockingScheduler
from django.db import transaction
from django.utils import timezone

os.environ["DJANGO_SETTINGS_MODULE"] = "requester.settings"
django.setup()

from rest_request.enums import HTTPMethods
from rest_request.models import RESTRequest, RESTResponse

scheduler = BlockingScheduler()

METHODS = {
    HTTPMethods.GET: requests.get,
    HTTPMethods.POST: requests.post,
    HTTPMethods.PATCH: requests.patch,
    HTTPMethods.DELETE: requests.delete,
}

logger = logging.getLogger(__name__)


@scheduler.scheduled_job('interval', seconds=3)
def send_requests():
    logger.info('Started task send_requests')

    started = timezone.now()

    rest_requests = RESTRequest.objects.select_for_update().filter(started__lte=started, completed=None)
    with transaction.atomic():
        for rest_request in rest_requests:
            logger.info(rest_request)
            requests_func = METHODS[rest_request.method]
            try:
                response = requests_func(rest_request.url, rest_request.data)
            except Exception as exc:
                logger.error(exc)
                headers = None
                status_code = 404
                data = None
            else:
                headers = dict(response.headers)
                status_code = response.status_code
                try:
                    data = json.loads(response.text)
                except JSONDecodeError:
                    data = response.text

            rest_response = RESTResponse.objects.create(
                headers=headers,
                status_code=status_code,
                data=data,
                rest_request_id=rest_request.id,
            )

            logger.info(rest_response)
            rest_request.completed = timezone.now()
            rest_request.save()

    logger.info('Ended task send_requests')


scheduler.start()
