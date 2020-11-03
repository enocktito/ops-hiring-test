from django.db import models


class CommentManager(models.Manager):
    pass


class Comment(models.Model):
    event = models.ForeignKey('event.Event', on_delete=models.CASCADE)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    message = models.CharField(max_length=130)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CommentManager()

    class Meta:
        db_table = '"event"."comment"'
        managed = True
