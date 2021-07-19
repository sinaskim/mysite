from django import forms #django로부터 forms를 불러온다.
from .models import Blog,Comment,Hashtag #.models로부터 Blog를 불러온다.

class PostForm(forms.ModelForm): #POSTFORM을 선언한다.
    class Meta: 
        model = Blog #model에 Blog 객체를 저장한다. 
        fields = ['title','writer','content','hashtags','image'] #fields에 title,writer,content 배열을 만든다.

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['name']