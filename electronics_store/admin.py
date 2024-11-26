from django.contrib import admin
from django.db import models
from django.db.models import QuerySet
from django.utils.html import format_html
from electronics_store.models import NetworkMember, ContactsInfo, Item
from typing import Tuple, List, Union

class ContactsInline(admin.TabularInline):

    model: models.Model = ContactsInfo
    extra = 0


class ItemsInline(admin.TabularInline):

    model: models.Model = Item
    extra = 0


class NetworkMemberAdmin(admin.ModelAdmin):

    inlines: List[admin.TabularInline] = [ContactsInline, ItemsInline,]
    list_display: Tuple[str, ...] = ("id", "name", "level", "to_supplier", "debt")
    list_display_links: Tuple[str, ...] = ('name', 'to_supplier')
    list_filter: Tuple[str, ...] = ('contactsinfo__city', )
    fields: List[Union[Tuple[str, ...], str]] = [("id", "name"), ("level", "supplier"), "debt", "date_of_creation"]
    readonly_fields: Tuple[str, ...] = ("id", "date_of_creation",)
    search_fields: Tuple[str, ...] = ("name",)
    save_on_top: bool = True
    actions: List[str] = ['clear_dept']

    def to_supplier(self, obj: NetworkMember):
        if obj.supplier is not None:
            return format_html(
                '<a href="/admin/electronics_store/networkmember/{id}">{name}</a>',
                id=obj.supplier.id,
                name=obj.supplier
            )


    @admin.action(description='clear debt')
    def clear_dept(self, request, queryset: QuerySet) -> None:
        queryset.update(debt=0)


class ItemAdmin(admin.ModelAdmin):

    list_display: Tuple[str, ...] = ("name", "model", "release_date", "owner")
    list_display_links = ('name', 'owner')
    search_fields: Tuple[str, ...] = ("name", "model", "release_date")
    save_on_top = True


admin.site.register(NetworkMember, NetworkMemberAdmin)
admin.site.register(Item, ItemAdmin)