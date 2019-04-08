from django.contrib import admin
from .models import Article

# Article 모델을 관리자 페이지(admin site)에서 확인하고 싶다.
admin.site.register(Article)
