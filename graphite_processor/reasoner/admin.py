from django.contrib import admin

from django.utils.translation import ugettext_lazy as _

from graphite_processor.reasoner.models import Check, Alert

class CheckAdmin(admin.ModelAdmin):
    list_display = ['metric', 'threshold', 'condition']
    list_editable = ['threshold', 'condition']
admin.site.register(Check, CheckAdmin)

class AlertAdmin(admin.ModelAdmin):
    list_display = ['check', 'received']
admin.site.register(Alert, AlertAdmin)
