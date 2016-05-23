from django.db import connections
from django.db.models import EmailField
from django.db.models.signals import pre_migrate
from django.dispatch import receiver


# Python 2/3 compatibility. Credit to https://github.com/oxplot/fysom/issues/1
try:
    unicode = unicode
except NameError:
    # 'unicode' is undefined, must be Python 3
    str = str
    unicode = str
    bytes = bytes
    basestring = (str, bytes)
else:
    # 'unicode' exists, must be Python 2
    str = str
    unicode = unicode
    bytes = str
    basestring = basestring


@receiver(pre_migrate)
def setup_postgres_extensions(sender, **kwargs):
    conn = connections[kwargs['using']]
    if conn.vendor == 'postgresql':
        cursor = conn.cursor()
        cursor.execute("CREATE EXTENSION IF NOT EXISTS citext")


class CiEmailField(EmailField):
    """A case insensitive EmailField.

    It uses the CITEXT extension on postgresql and lowercases the value on
    other databases.

    """
    def db_type(self, connection):
        if connection.vendor == 'postgresql':
            return 'CITEXT'
        return super(CiEmailField, self).db_type(connection)

    def get_db_prep_value(self, value, connection, prepared=False):
        if connection.vendor != 'postgresql':
            if isinstance(value, basestring):  # value might be None
                value = value.lower()
        return super(CiEmailField, self).get_db_prep_value(
            value, connection, prepared)
