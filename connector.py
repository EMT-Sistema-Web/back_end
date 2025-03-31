# machbase/proxy/connector.py
import pyodbc
from django.conf import settings
from django.db import models

class MachbaseConnection:
    _connection = None

    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            cls._connection = pyodbc.connect(
                f'DRIVER={settings.MACHBASE_DRIVER};'
                f'SERVER={settings.MACHBASE_HOST};'
                f'PORT={settings.MACHBASE_PORT};'
                f'UID={settings.MACHBASE_USER};'
                f'PWD={settings.MACHBASE_PASSWORD};'
                f'DATABASE={settings.MACHBASE_DB}'
            )
        return cls._connection

    @classmethod
    def close_connection(cls):
        if cls._connection is not None:
            cls._connection.close()
            cls._connection = None