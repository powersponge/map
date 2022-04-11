from django.contrib import admin
from .models import *


@admin.register(도_광역시)
class 도_광역시Admin(admin.ModelAdmin):
    list_display = ['번호', '이름']
    list_display_links = ['번호', '이름']
    list_per_page = 20
    
    



@admin.register(지역)
class 지역Admin(admin.ModelAdmin):
    list_display = ['번호', '이름']
    list_display_links = ['번호', '이름']
    list_per_page = 20
    list_filter = ['도_광역시']
    search_fields = ['번호','이름','도_광역시']
    

@admin.register(재활센터)
class 재활센터Admin(admin.ModelAdmin):
    fields = ['번호','이름','지역','주소','웹사이트','정보','위도','경도','센터','가정방문','전화번호','사진']
    list_display = ['번호', '이름']
    list_display_links = ['번호', '이름']
    list_per_page = 20
    list_filter = ['지역']
    search_fields = ['번호','이름','주소']


