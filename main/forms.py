from django import forms
# from .models import Snippet
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class Form1(forms.Form):
	name = forms.CharField()
	email = forms.EmailField(label = 'Email')
	category = forms.ChoiceField(choices = [('question', 'Question'), ('other', 'Other')])
	subject = forms.CharField(required = False)
	body = forms.CharField(widget = forms.Textarea)
	Submit('submit', 'Generate PDF', css_class='btn-success')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.helper = FormHelper
		self.helper.form_method = 'post'

		self.helper.layout = Layout(
			'name',
			'email',
			'category',
			'subject',
			'body',
			Submit('submit', 'Generate PDF', css_class='btn-success')
			)
