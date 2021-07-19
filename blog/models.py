from django.db import models # django.db로부터 models를 불러와라
from django.conf import settings # django.conf로부터 settings를 불러와라
# Create your models here.

class Blog(models.Model): #클래스 Blog 선언
    title = models.CharField(max_length=200) #제목은 최대길이 200으로 charfield로 받는다.
    pub_date = models.DateField('date published') #날짜와 시간은 model의 datefield로 작성된다.
    writer = models.CharField(max_length=15, default='닉네임을 입력해주세요') #글쓴이는 model의 charfield로 받되, 최대길이는 15이고 이름을 입력하기 이전에 '닉네임을 입력해주세요'를 먼저 띄운다.
    content = models.TextField() # 내용을 model의 textfield를 이용하여 받는다. 글자제한 x
    hashtags = models.ManyToManyField('Hashtag', blank=True)
    image = models.ImageField(upload_to='images/', blank = True)

    def __str__(self): #함수 __str__선언
        return self.title # 게시물의 제목을 입력한대로 반환한다.

class Comment(models.Model):
    def __str__(self):
        return self.text
        
    post_id = models.ForeignKey(Blog,on_delete=models.CASCADE, related_name = 'comments')
    text = models.CharField(max_length=50)

class Hashtag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

