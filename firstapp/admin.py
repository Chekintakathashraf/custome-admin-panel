from django.contrib import admin
from .models import Customer, Order 
from django import forms

class CustomerForms(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        widgets = {
            'address' : forms.Textarea(attrs={'rows':3, 'cols':9})
        }


class OrderInline(admin.TabularInline):
    model = Order
    extra = 0

# class OrderInline(admin.StackedInline):
#     model = Order
#     extra = 0
    

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    form = CustomerForms   #for customising the forms in admin styling
    list_display = [
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "address",
    ]
    search_fields = [
         "first_name",
        "last_name",
        "email",
        "phone_number",
        "address",
    ]
    
    inlines = [OrderInline]


# admin.site.register(Order)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "customer",
        "order_date",
        "total_amount",
        "status",
    ]
    list_filter = [
        "status",
    ]
    
    #for search in forekey dropdown
    search_fields = [
        "customer__first_name",
        "customer__last_name",
    ]
    autocomplete_fields = [
        "customer",
    ]
    
    
    exclude = [
        "total_amount",
    ]
    readonly_fields = [
        "order_date",
    ]
    
    actions = [
        "mark_as_shipped",
    ]
    
    def mark_as_shipped(self,request,queryset):
        queryset.update(status = "Shipped")
        
    mark_as_shipped.short_description = "Mark selected order as shipped"