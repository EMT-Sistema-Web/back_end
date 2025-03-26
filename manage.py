#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from django.db import models
from .connector import MachbaseConnection

class MachbaseManager(models.Manager):
    def __init__(self, table_name=None, *args, **kwargs):
        self.table_name = table_name
        super().__init__(*args, **kwargs)

    def get_queryset(self):
        # Retorna um queryset vazio pois substituiremos todos os métodos
        return super().get_queryset().none()

    def filter(self, **kwargs):
        """Simula o método filter do QuerySet"""
        where_clause = ' AND '.join([f"{k} = ?" for k in kwargs.keys()])
        query = f"SELECT * FROM {self.table_name}"
        if where_clause:
            query += f" WHERE {where_clause}"
        
        conn = MachbaseConnection.get_connection()
        cursor = conn.cursor()
        cursor.execute(query, list(kwargs.values()))
        
        results = []
        for row in cursor:
            results.append(self.model.from_db_row(row))
        return results

    def all(self):
        """Retorna todos os registros"""
        return self.filter()
    
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'emt_web_system.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
