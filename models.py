# Create your models here.
from django.db import models
from products.models import Product, Category
from providers.models import Provider

"""
Stock model
Models that delivers the information for the stock on an inventory
"""
class Stock_real( models.Model ) :
    
    product = models.ForeignKey( Product, default = 1 )
    quantity = models.DecimalField( max_digits= 19, decimal_places = 2, 
        default = 0.0 )
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )
    
    def __unicode__( self ) :
        """ unicode function for the printing of the stock """
        return ( "P:{0}, Q:{1}" ).format( self.product.name, self.quantity )
    
    #End of unicode function
    
#End of stock model

"""
Invetory
Inventory model, it will link a lot of products
"""
class Inventory_real( models.Model ) :
    
    name = models.CharField( max_length = 200, unique = True )
    description = models.CharField( max_length = 1000, default='' )
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )
    stocks = models.ManyToManyField( Stock_real, verbose_name="list of stocks" )
    
    def __unicode__( self ) :
        """  unicode function for the printing of the inventory """
        return self.name
    
    #End of unicode function
    
#End of inventory Model

"""
Purchase_real
Model that saves a purchase to a provider
"""
class Purchase_real( models.Model ) :
    
    provider = models.ForeignKey( Provider, default = 1 )
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )
    
    def __unicode__( self ) :
        """ unicode function for the printing of the purchase """
        return ( "#{0}-Pruchase from {1}" ).format( self.id, self.provider.name )

    #End of unicode function
    
#End of purchase_real model

"""
Detail_purshase_real
Model that details the purchase_real
"""
class Detail_purchase_real( models.Model ) :
    
    purchase_real = models.ForeignKey( Purchase_real, default = 1 )
    product = models.ForeignKey( Product, default = 1 )
    purchase_price = models.DecimalField( max_digits = 19, decimal_places = 2, 
        default = 0.0 )
    quantity = models.DecimalField( max_digits = 19, decimal_places = 2, 
        default = 0.0 )
    
    def save( self ) :
        """ 
        Save, this function will edit the buy_price of the product and then it 
        will save the product and then the detail 
        """
        self.product.buy_price = self.purchase_price
        self.product.save()
        super( Detail_purchase_real, self ).save()
    
    #End of save function
    
    def __unicode__( self ) :
        """ unicode function for the printing of the detail """
        return ( '{0}' ).format( self.product.name )
    
    #End of unicode function
        
#End of Detail purchase_real model