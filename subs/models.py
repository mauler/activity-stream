from django.db import models
from django.contrib.auth.models import User

# from django.contrib.auth import get_user_model
# User = get_user_model()

from django.db.models.signals import post_save
from actstream import action


class Post(models.Model):
    text = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.text


def new_post(sender, instance, created, **kwargs):
    action.send(instance.user, verb='posted', target=instance, mood='sleepy')


post_save.connect(new_post, sender=Post)


class Profile(models.Model):
    private = models.BooleanField(default=False)
    user = models.OneToOneField(User)

    def __unicode__(self):
        return str(self.user)