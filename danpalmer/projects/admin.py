from django.contrib import admin

from .models import Contribution


class ContributionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'source_url',
        'created',
    )
    date_hierarchy = 'created'


admin.site.register(Contribution, ContributionAdmin)
