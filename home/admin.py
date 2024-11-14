from django.contrib import admin
from .models import SurveyResponse, SurveyStartJob
from import_export.admin import ImportExportModelAdmin, ExportMixin

from .resources import SurveyResource


class SurveyInlineAdmin(admin.TabularInline):
    model = SurveyStartJob
    fields = ('unit', 'start1', 'end1', 'organ1')
    readonly_fields = ('unit', 'start1', 'end1', 'organ1')
    extra = 0

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj):
        return False


@admin.register(SurveyResponse)
class SurveyResponseAdmin(ExportMixin, admin.ModelAdmin):
    inlines = [SurveyInlineAdmin]
    resource_class = SurveyResource
    list_display = (
        'fullname', 'company', 'registerDate', 'fieldstudy', 'Grade', 'univercity', 'is_read')
    list_filter = ('company', 'Grade', 'is_read')
    search_fields = ('fullname',)
