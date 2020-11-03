import binascii
import os

from django.db import models
from django.conf import settings


class AuthToken(models.Model):
    key = models.CharField(max_length=40)
    refresh = models.CharField(max_length=40, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
            self.refresh = self.generate_key()
        return super().save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def regenerate(self, force_refresh=False):
        if settings.TESTING:
            return
        self.key = self.generate_key()
        if force_refresh:
            self.refresh = self.generate_key()
        self.save()

    def __str__(self):
        return self.key

    db_table = '"event"."auth_token"'
    managed = True
