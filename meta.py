# machbase/proxy/meta.py
from django.db.models.options import Options

class MachbaseMeta(Options):
    def __init__(self, meta, cls):
        super().__init__(meta)
        self.model = cls
        self.app_label = cls.__module__.split('.')[0]
        self.object_name = cls.__name__
        self.verbose_name = getattr(meta, 'verbose_name', self.object_name.lower())
        self.verbose_name_plural = getattr(meta, 'verbose_name_plural', self.verbose_name + 's')
        self.managed = getattr(meta, 'managed', False)