from django.db import models

class 도_광역시(models.Model):
    이름 = models.CharField(max_length=40)
    

class 지역(models.Model):
    이름 = models.CharField(max_length=40)
    도_광역시 = models.ForeignKey(도_광역시, on_delete=models.CASCADE)
    
class 재활센터(models.Model):
    이름 = models.CharField(max_length=70)
    주소 = models.CharField(max_length=200)
    정보= models.CharField(max_length=1400)
    싸이트= models.CharField(max_length=200)
    위도= models.CharField(max_length=200)
    경도= models.CharField(max_length=200)
    센터= models.BooleanField(default=False)
    가정방문= models.BooleanField(default=False)
    전화번호= models.CharField(max_length=60)
    지역 = models.ForeignKey(지역, on_delete=models.CASCADE)


