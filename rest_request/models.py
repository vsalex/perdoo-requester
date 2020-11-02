from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE

from core.models import DatetimeMixin
from rest_request.enums import HTTPMethods


class RESTRequest(DatetimeMixin):
    started = models.DateTimeField(
        null=True,
        blank=True,
        default=None,
        help_text='When the request will start'
    )
    completed = models.DateTimeField(
        null=True,
        blank=True,
        default=None,
        help_text='When the request is completed',
    )

    method = models.CharField(
        max_length=6,
        choices=HTTPMethods.choices,
        default=HTTPMethods.GET,
    )
    url = models.URLField(
        null=False,
        blank=False,
    )
    data = models.JSONField(
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        User,
        related_name='rest_requests',
        null=False,
        blank=False,
        on_delete=CASCADE,
        help_text='The user who created the request'
    )

    @property
    def is_completed(self):
        return bool(self.completed)

    def __str__(self):
        return f'REST Request (started={self.started}, completed={self.completed})'


class RESTResponse(DatetimeMixin):
    headers = models.JSONField(null=True)
    status_code = models.PositiveSmallIntegerField()
    data = models.JSONField(null=True)

    rest_request = models.OneToOneField(
        RESTRequest,
        related_name='rest_response',
        null=False,
        blank=False,
        on_delete=CASCADE,
    )

    def __str__(self):
        return f'REST Response (status_code={self.status_code}, request_id={self.rest_request.id})'
