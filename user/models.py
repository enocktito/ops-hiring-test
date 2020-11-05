import os

from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models
from django.utils.timezone import now


def _content_file_name(instance, filename):
    filename = "%s_%s" % (now().isoformat(), filename)
    return os.path.join('user', filename)


class EventUserManager(UserManager):
    pass


class User(AbstractUser):
    photo = models.ImageField(null=True, upload_to=_content_file_name)
    updated = models.DateTimeField(auto_now=True, )
    email = models.EmailField(unique=True)

    objects = EventUserManager()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        db_table = 'event_user'
        managed = True
