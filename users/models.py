from django.db import models

from django.utils.translation import gettext_lazy as _

class MyModel(models.Model):
    name = models.CharField(_("Name"), max_length=255)