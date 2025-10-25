from django.contrib import admin
from website.models import Contact


# Register your models here.
@admin.register(Contact)
class ContantAdmin (admin.ModelAdmin):
    date_hierarchy = 'create_date'
    empty_value_display = "-empty-"
    list_display = ["name", 'subject', 'email']
    search_fields = ["name", "subject", "message"]
    list_filter = ("subject", "email",)
