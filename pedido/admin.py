from django.contrib import admin

from .models import Pedido, ItemPedido


class itemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1


class PedidoAdmin(admin.ModelAdmin):
    inlines = [
        itemPedidoInline
    ]


admin.site.register(Pedido, PedidoAdmin)
admin.site.register(ItemPedido)
