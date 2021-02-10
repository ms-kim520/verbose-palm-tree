from django.conf import settings
from django.db import models

# Create your models here.

class Post(models.Model):
    #각 데이터에 대한 제한 조건도 함께 설정
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE) #글쓴이는 외래키를 가진다./ AUTH_USER_MODEL 기본 유저 모델로, 자동으로 작성자 목록 테이블에 연결해주기 위해 외래키로 설정
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True) #내용은 비어있어야 한다. 
    created_date = models.DateTimeField(auto_now_add=True) #자동으로 현재날짜로 생성
    published_date = models.DateTimeField(blank=True,null=True) #게시 날짜


