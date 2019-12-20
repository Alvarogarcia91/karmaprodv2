
from django.contrib import admin
from .models import Cart,CartItem
from import_export.admin import ImportExportModelAdmin

# class CartAdmin(admin.ModelAdmin):
# 	# list_display = ['name','slug']
# 	# prepopulated_fields = {'slug':('name',)}
# admin.site.register(Cart,CartAdmin)

# class CartItemAdmin(admin.ModelAdmin):
# 	# list_display = ['name','price','stock','available','created','updated']
# 	# list_editable = ['price','stock','available']
# 	# prepopulated_fields = {'slug':('name',)}
# 	# list_per_page = 20
# admin.site.register(CartItem,CartItemAdmin)



@admin.register(
    Cart,
    CartItem,
    


    
    )
class ViewAdmin(ImportExportModelAdmin):
    pass


