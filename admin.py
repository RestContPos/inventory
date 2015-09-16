from django.contrib import admin
from .models import Inventory_real, Stock_real, Purchase_real, Detail_purchase_real
from .forms import Inventory_realForm, Stock_realForm, Purchase_realForm, Detail_purchase_realForm

"""
Admin module for the inventory shit
"""
class Inventory_realAdmin( admin.ModelAdmin ) :
    
    list_display = [ 'name', 'description', 'timestamp', 'updated' ]
    form = Inventory_realForm
        
#End of invetory Admin class

"""
Admin module for stock shit
"""
class Stock_realAdmin( admin.ModelAdmin ) :
    
    list_display = [ 'product', 'quantity' ]
    form = Stock_realForm
    
#End of stock admin class

"""
Purchase_realAdmin 
"""
class Purchase_realAdmin( admin.ModelAdmin ) :
    
    list_display = [ 'id', 'provider', 'timestamp', 'updated' ]
    form = Purchase_realForm
    
#End Purchase_realAdmin Class

"""
Detail_purchase_realAdmin
"""
class Detail_purchase_realAdmin( admin.ModelAdmin ) :
    
    list_display = [ 'id', 'purchase_real', 'product', 'purchase_price', 'quantity' ]
    form = Detail_purchase_realForm

#End of Detail_purchase_realAdmin class

admin.site.register( Inventory_real, Inventory_realAdmin )
admin.site.register( Stock_real, Stock_realAdmin )
admin.site.register( Purchase_real, Purchase_realAdmin )
admin.site.register( Detail_purchase_real, Detail_purchase_realAdmin )
