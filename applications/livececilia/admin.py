from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from applications.livececilia.models import LiveCecilia


class LiveCeciliaResource(resources.ModelResource):

    class Meta:
        model = LiveCecilia
        exclude = ('imported', )
        fields = ('firstname', 'lastname', 'date_nac', 'genere', 'code_zip',
                  'city', 'email', 'phone', 'created_at',)
        export_order = ('email', )


class LiveCeciliaAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = ('firstname', 'lastname', 'date_nac', 'genere', 'code_zip',
                    'city', 'email', 'phone', 'created_at')
    search_fields = ('firstname', 'lastname', 'email',)
    ordering = ('firstname', 'lastname', )


admin.site.register(LiveCecilia, LiveCeciliaAdmin)
