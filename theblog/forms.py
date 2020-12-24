from django import forms
from .models import Post, Category


choices = Category.objects.all().values_list('cat_name', 'cat_name')
choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'author', 'body','header_image' )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category' : forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control','value': '', 'id':'elder','type':'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['content'].label = "What do you want to say?"
