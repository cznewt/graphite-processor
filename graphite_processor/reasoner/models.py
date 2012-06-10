# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from graphite_processor.collector.models import Metric

CONDITION_CHOICES = (
    ('gt', 'Greater'),
    ('gteq', 'Greater or equal'),
    ('eq', 'Equal'),
    ('lteq', 'Lower or equal'),
    ('lt', 'Lower'),
)

SEVERITY_CHOICES = (
    (0, 'Info'),
    (1, 'Wanring'),
    (2, 'Error'),
)

class Check(models.Model):
    metric = models.ForeignKey(Metric, verbose_name=_("metric"))
    threshold = models.DecimalField(max_digits=20, decimal_places=4, verbose_name="threshold")
    condition = models.CharField(max_length=55, verbose_name="condition", choices=CONDITION_CHOICES, default="greater_than")
    severity = models.IntegerField(verbose_name="severity", choices=SEVERITY_CHOICES, default='warning')
    escalates = models.ForeignKey('self', verbose_name=_("escalates check"), blank=True, null=True)
    label = models.CharField(max_length=55, verbose_name="check label", blank=True, null=True)
    active = models.BooleanField(verbose_name="is active?", default=True)

    def __unicode__(self):
        return u'%s:%s' % (self.metric, self.threshold)

    class Meta:
        verbose_name = _("check")
        verbose_name_plural = _("checks")

class Alert(models.Model):
    check = models.ForeignKey(Check, verbose_name=_("check"))
    received = models.DateTimeField(verbose_name="received")
    resolved = models.DateTimeField(verbose_name="esolved", blank=True, null=True)
    counter = models.IntegerField(verbose_name=_("count"), default=1)
    escalates = models.ForeignKey('self', verbose_name=_("escalates"), blank=True, null=True)
    acknowledged = models.BooleanField(verbose_name="is acknowledged?", default=False)

    def __unicode__(self):
        return u'%s:%s' % (self.received, self.check)

    class Meta:
        verbose_name = _("alert")
        verbose_name_plural = _("alerts")
