import uuid

from django.db.models import DateField, DateTimeField
from django.utils import timezone
from django.utils.text import slugify

from unidecode import unidecode


def generate_uuid_without_hyphens() -> str:
    """Generate UUID value, but remove all hyphen characters in it."""
    return str(uuid.uuid4().hex)


def slugify_value_to_ASCII(val: str) -> str:
    """
    Slugify is converting value to lowercase and replacing spaces with hyphen,
    but also removing accents and special characters of some languages (such as Vietnamese) for a correct slug value.
    """
    return slugify(unidecode(val))


def customize_datetime_display(obj, field, custom_format=None):
    field_value = field.value_from_object(obj)

    if custom_format is None:
        if isinstance(field, DateTimeField):
            custom_format = "%H:%M, %d/%m/%Y"
            local_datetime = timezone.localtime(field_value)
            return local_datetime.strftime(format=custom_format)
        elif isinstance(field, DateField):
            custom_format = "%d/%m/%Y"

    return field_value.strftime(format=custom_format)
