# -#- coding: utf-8 -#-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from webcms.models import Widget
from graphite_processor.grapher.models import Graph

class LinearGraphWidget(Widget):
    graph = models.ForeignKey(Graph, verbose_name=_('graph'))

    def lines(self):
        return self.graph.line_set.all()

    class Meta:
        abstract = True
        verbose_name = _('linear graph')
        verbose_name_plural = _('linear graphs')
