from django.contrib import admin

from django.utils.translation import ugettext_lazy as _

from graphite_processor.collector.models import Metric

class MetricAdmin(admin.ModelAdmin):
    list_display = ['label', 'target', 'active']
admin.site.register(Metric, MetricAdmin)
