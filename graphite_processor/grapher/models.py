# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from graphite_processor.collector.models import Metric

COLOR_CHOICES = (
    ('red', 'Red'),
    ('blue', 'Blue'),
    ('green', 'Green'),
)

class Graph(models.Model):
    label = models.CharField(max_length=55, verbose_name="graph label")
    area_mode = models.CharField(max_length=55, verbose_name="area mode", default='none')
    line_mode = models.CharField(max_length=55, verbose_name="line mode", default='slope')
    y_axis_label = models.CharField(max_length=55, verbose_name="Y axis title")

    def __unicode__(self):
        return u'%s' % self.label

    class Meta:
        verbose_name = _("graph")
        verbose_name_plural = _("graphs")

class Line(models.Model):
    graph = models.ForeignKey(Graph)
    metric = models.ForeignKey(Metric)
    color = models.CharField(max_length=55, verbose_name="color", default='red', choices=COLOR_CHOICES)

    def __unicode__(self):
        return u'%s:%s' % (self.graph, self.series)

    class Meta:
        verbose_name = _("graph line")
        verbose_name_plural = _("graph lines")
