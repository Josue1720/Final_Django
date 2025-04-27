from django import forms
from .models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
        labels = {
            'product_id': 'Product ID',
             'name' : 'Product Name',
             'sku' : 'Stock Keeping Unit',
             'price' : 'Price',
             'quatity' : 'Quantity',
             'supplier_name' : 'Supplier Name'
        }

        widgets ={
            'product_id' : forms.NumberInput(
                attrs={
                    'placeholder': 'e.g 1', 'class':'form-control',
                }
            ),
            'name' : forms.TextInput(
                attrs={
                    'placeholder': 'Laptop', 'class':'form-control',
                }
            )
            ,
            'sku' : forms.TextInput(
                attrs={
                    'placeholder': 'e.g 12345', 'class':'form-control',
                }
            )
            ,
            'price' : forms.NumberInput(
                attrs={
                    'placeholder': 'e.g 1', 'class':'form-control',
                }
            )
            ,
            'quantity' : forms.NumberInput(
                attrs={
                    'placeholder': 'e.g 1', 'class':'form-control',
                }
            )
             ,
            'supplier_name' : forms.TextInput(
                attrs={
                    'placeholder': 'ABC Corp', 'class':'form-control',
                }
            )
        }
        
class LoginForm(forms.Form): #forms for login
    username=forms.CharField(
        widget=forms.TextInput( 
             attrs={
              'placeholder':'username',
             'class':'form-control'   ,             
             })
    )
    password= forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'password',
                 'class':'form=control',
            }
        )
    )
    
    