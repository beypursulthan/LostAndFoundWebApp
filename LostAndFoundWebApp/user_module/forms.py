from django import forms
from .models import UserLostItem, UserFoundItem


class UserLostItemForm(forms.ModelForm):
    class Meta:
        model = UserLostItem
        fields = ['item_name', 'description', 'location']


class UserFoundItemForm(forms.ModelForm):
    class Meta:
        model = UserFoundItem
        fields = ['item_name', 'description', 'location']
