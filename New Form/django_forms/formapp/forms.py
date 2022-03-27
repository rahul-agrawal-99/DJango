
from django import forms
from .models import Contact
from crispy_forms.helper import FormHelper


from crispy_forms.layout import Layout, Submit, Row, Column

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(label='Enter Email here')
    message = forms.CharField(widget=forms.Textarea)
    choise  = forms.ChoiceField(choices=[('one','1'),('two','2'),('three','3')])  # [("value" , "lable")]
    
    
class SubmitForm(forms.ModelForm):
    def __init__(self , *args , **kwargs):
        super(SubmitForm , self).__init__(*args , **kwargs)
        self.helper = FormHelper(self)
        
        self.helper.form_method = 'post'
        
        self.helper.layout = Layout(
            'name' ,
            'email' ,
            'message' ,
            Submit('submit', 'Submit', css_class='btn-primary')
        )
    class Meta:
        model = Contact
        fields = {'name', 'email', 'message'}
        



# class ContactForm(forms.ModelForm):
#     def __init__(self , *args , **kwargs):
#         super().__init__(*args , **kwargs)
#         self.helper = FormHelper(self)
        
#         self.hepler.form_method = 'post'
        
#         self.helper.layout = Layout(
#             'name' ,
#             'email' ,
#             'message' ,
#             'choise' ,
#             Submit('submit', 'Submit', css_class='btn-primary')
#         )
#     class Meta:
#         model = Contact
#         fields = {'name', 'email', 'message'}
    
    
# class SubmitForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         fields = {'name', 'email', 'message'}