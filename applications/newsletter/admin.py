from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from applications.newsletter.models import Newsletter


class NewsletterResource(resources.ModelResource):

    class Meta:
        model = Newsletter
        exclude = ('imported', )
        fields = ('email',)
        export_order = ('email', )


class NewsletterAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = ('email', 'created_at')
    search_fields = ('email',)
    ordering = ('created_at', )


admin.site.register(Newsletter, NewsletterAdmin)
