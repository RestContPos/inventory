from django import forms
from .models import Inventory_real, Stock_real, Detail_purchase_real, Purchase_real

"""
InventoryForm
General form inventry
"""
class Inventory_realForm( forms.ModelForm ) :
    
    description = forms.CharField( widget=forms.Textarea )
    
    class Meta :
        
        model = Inventory_real
        fields = [ "name", 'description', 'stocks' ]
    
#End of inventory form class

"""
Stock form
"""
class Stock_realForm( forms.ModelForm ) :
    
    class Meta :
        
        model = Stock_real
        fields = [ "product", "quantity" ]
    
    #End of Meta class

#End of stock form function

"""
Purchase_realForm
"""
class Purchase_realForm( forms.ModelForm ) :
    
    class Meta :
        
        model = Purchase_real
        fields = [ "provider" ]
        
    #End of Meta class
    
#End of Purchase_realForm class

"""
Detail_purchase_real form
"""
class Detail_purchase_realForm( forms.ModelForm ) :

    class Meta :
        
        model = Detail_purchase_real
        fields = [ "product", "purchase_real", "purchase_price", "quantity"]
    
    #End of meta class
    
#End of Detail purchase realForm