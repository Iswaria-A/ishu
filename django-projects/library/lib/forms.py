from django import forms
class AddForm(forms.Form):
	lib_name=forms.CharField(label='Lib Name')
	lib_author_name=forms.CharField(label='Lib Authorname')
	lib_year=forms.IntegerField(label='Lib Year')
	lib_price=forms.IntegerField(label='Lib Price')