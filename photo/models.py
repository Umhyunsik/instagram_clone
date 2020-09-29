from django.db import models

# Create your models here.

# 1. 모델 : 데이터 베이스에 저정될 데이터가 있다면 해당 데이터를 묘사한다.
# 2. 뷰 (기능) : 계산, 처리 - 실제기능 ,화면
# 3. URL 맵핑 : 라우팅 테이블에 기록한다. urls.py에 기록 - 주소를 지정
# 4. 화면에 보여줄 것이있다. : 템플릿 작성(html)

# 장고의 기본 유저 모델
from django.contrib.auth.models import User
from django.urls import reverse
#author photo text created updated

class Photo(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE , related_name='user_photos')
    # 외래키(ForeignKey) - User 테이블에서 해당 유저를 찾을 수 있는 주 키
    photo=models.ImageField(upload_to='photos/%Y/%m/%d',default='photos/no_image.png')
    text = models.TextField()
    created= models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    #변경사항 저장 -> db에 반영
    # makemigrations -> migrate
    class Meta:
        ordering=['-updated']
    def __str__(self):
        #관리자페이지에서 출력할때
        return self.author.username + " " +self.created.strftime("%Y-%m-%d %H:%M:%S")
    def get_absolute_url(self):
        #작성하고나 수정하고나면 어디로갈꺼야
        return reverse('photo:photo_detail',args=[self.id])



