
from django.db import models
from .manage import MachbaseManager
from django.db import models
from .manage import MachbaseManager
from .meta import MachbaseMeta

class MachbaseModel(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._meta = MachbaseMeta(self._meta, self.__class__)

    class Meta:
        abstract = True
        managed = False

    # ... (restante do código anterior)
class MachbaseModel(models.Model):
    _meta = None  # Será configurado dinamicamente

    class Meta:
        abstract = True
        managed = False

    @classmethod
    def from_db_row(cls, row):
        """Cria uma instância do modelo a partir de uma linha do banco"""
        instance = cls()
        for i, field in enumerate(cls._meta.fields):
            setattr(instance, field.name, row[i])
        return instance

    def save(self, *args, **kwargs):
        raise NotImplementedError("O proxy é somente leitura")

    def delete(self, *args, **kwargs):
        raise NotImplementedError("O proxy é somente leitura")