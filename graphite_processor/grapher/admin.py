from django.contrib import admin

from django.utils.translation import ugettext_lazy as _

from graphite_processor.grapher.models import Line, Graph

class Line_Inline(admin.TabularInline):
    model = Line
    extra = 5

class LineAdmin(admin.ModelAdmin):
    list_display = ['graph', 'metric', 'color']
    list_filter = ['graph',]
admin.site.register(Line, LineAdmin)

class GraphAdmin(admin.ModelAdmin):
    list_display = ['label', 'area_mode', 'line_mode', 'y_axis_label']
    list_editable = ['area_mode', 'line_mode',]
    inlines = [Line_Inline, ]
admin.site.register(Graph, GraphAdmin)
