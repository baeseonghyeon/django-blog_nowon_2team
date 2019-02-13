from django import forms
from .models import Blog

#class BlogPost(forms.Form) #모델 기반이 아닌 임의의 입력공간일 경우

class BlogPost(forms.ModelForm): 
    class Meta:
        model = Blog #blog 모델의
        fields = ['title', 'body'] #title과 body를 입력받을 공간



