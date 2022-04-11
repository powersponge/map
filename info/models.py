""" f"{self.id} {self.이름}" """

from django.db import models


class 도_광역시(models.Model):
    id = models.AutoField(primary_key=True)
    번호 = models.IntegerField(unique=True,blank=False, null=False)
    이름 = models.CharField(max_length=40)
    def __str__(self):
        return self.이름
    class Meta: 
        verbose_name_plural = "도_광역시"
        ordering = ['번호']


class 지역(models.Model):
    id = models.AutoField(primary_key=True)
    번호 = models.IntegerField(unique=True,blank=False, null=False)
    이름 = models.CharField(max_length=40)
    도_광역시 = models.ForeignKey(도_광역시, on_delete=models.CASCADE)
    def __str__(self):
        return self.이름
    class Meta: 
        verbose_name_plural = "소도시_지역"
        ordering = ['번호']

    
    
class 재활센터(models.Model):
    id = models.AutoField(primary_key=True)
    번호 = models.IntegerField(unique=True,blank=False, null=False)
    이름 = models.CharField(max_length=70)
    주소 = models.CharField(max_length=200)
    정보= models.TextField(max_length=1400)
    웹사이트= models.CharField(max_length=200)
    위도= models.CharField(max_length=200)
    경도= models.CharField(max_length=200)
    센터= models.BooleanField(default=False)
    가정방문= models.BooleanField(default=False)
    전화번호= models.CharField(max_length=60, blank=True, null=True)
    지역 = models.ForeignKey(지역, on_delete=models.CASCADE)
    사진 = models.ImageField(upload_to='images/',default="logo.png")
    def __str__(self):
        return self.이름
    class Meta: 
        verbose_name_plural = "재활센터"
        ordering = ['번호']

