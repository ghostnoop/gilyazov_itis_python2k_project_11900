from django.contrib import admin

from core.models import *


class PointAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "surname",
        "name",
        "last_name",
        "relation",
        "birth_date",
        "dead_date",
    )
    list_display_links = ("id", "name")
    search_fields = ("id", "name", "birth_date", "dead_date")
    list_editable = ("relation",)
    list_filter = ("birth_date", "dead_date", "relation")


class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "get_user_email", "created_at")

    # search_fields = ('id', 'email')

    def get_queryset(self, request):
        qs = super(ClientAdmin, self).get_queryset(request)
        return qs.select_related("user")

    def get_user_email(self, instance: Client):
        return instance.user.email

    get_user_email.admin_order_field = "user__email"
    get_user_email.short_description = "Почта пользователя"


admin.site.register(Client, ClientAdmin)
admin.site.register(ConfirmCode)
admin.site.register(ClientFeedBack)
admin.site.register(Executor)
admin.site.register(Service)
admin.site.register(Order)
admin.site.register(OrderStatus)
admin.site.register(Point, PointAdmin)
admin.site.register(PointPhoto)
admin.site.register(PointNotification)
admin.site.register(Relation)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Dispute)
admin.site.register(DisputeStatus)
admin.site.register(DisputeComment)
