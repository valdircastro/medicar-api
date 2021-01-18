from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date


def validate_present_or_future(value):
    if value < date.today():
        raise ValidationError(
            _('%(value)s is a past date'),
            params={'value': value},
        )
