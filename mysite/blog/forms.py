from django import forms  
from .models import Comment
  
  
class EmailPostForm(forms.Form):  
    name = forms.CharField(label= 'Ваше имя', max_length=25)  
    email = forms.EmailField(label= 'Ваш email')  
    to = forms.EmailField(label= 'Кому', )  
    comments = forms.CharField(label= 'Комментарий', required=False,  
			       widget=forms.Textarea)
    
class CommentForm(forms.ModelForm):  
    class Meta:  
        model = Comment  
        fields = ('name', 'email', 'body')



        