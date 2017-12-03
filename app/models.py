# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# from django.conf import settings
#
#
class UserData(models.Model):
    class Meta:
        db_table = "user_data"
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    telephone = models.TextField(blank=False)


    def __str__(self):
        return self.user

    def __unicode__(self):
        return "{0}, {1}".format(self.user, self.first_name, self.last_name, self.telephone)
#

