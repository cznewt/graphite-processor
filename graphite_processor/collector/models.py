# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Metric(models.Model):
    target = models.TextField(verbose_name=_("graphite target"))
    active = models.BooleanField(verbose_name=_("is active?"), default=True)
    label = models.CharField(max_length=55, verbose_name=_("metric label"), blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.target

    class Meta:
        verbose_name = _("metric")
        verbose_name_plural = _("metrics")
