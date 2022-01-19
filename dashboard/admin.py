from django.contrib import admin

# Register your models here.

from .models import Balance, Bitcoin, Transaction, Fusion, HubRequest

class BitcoinAdmin(admin.ModelAdmin):
  list_display = ('username', 'amount')

class HubRequestAdmin(admin.ModelAdmin):
  list_display = ('email', 'income', 'country', 'income')

# class BankAdmin(admin.ModelAdmin):
#   list_display = ('username', 'amount', )



admin.site.register(Bitcoin, BitcoinAdmin)
admin.site.register(HubRequest, HubRequestAdmin)


admin.site.register(Balance)
admin.site.register(Transaction)
admin.site.register(Fusion)
