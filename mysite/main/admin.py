from django.contrib import admin

from .models import Item




class ItemAdmin(admin.ModelAdmin):

    list_display =('user','task', 'complete')

admin.site.register(Item, ItemAdmin)
