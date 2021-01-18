from django.contrib import admin
from import_export.admin import ImportExportMixin

from .models import Order, Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["id", "brand", ]


@admin.register(Order)
class OrderAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ["id", "status", "client", "driver", "client_comment", "created_at"]
    list_filter = ["status", "created_at", ]
    list_editable = ["status"]
    search_fields = ["client__name", "driver_name", "address", ]
