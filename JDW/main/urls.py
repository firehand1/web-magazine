from django.contrib import admin
from django.urls import path
# index는 대문, blog는 게시판
from main.views import index, blog, posting, new_post, remove_post

# 이미지를 업로드
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('blog/<int:pk>/', posting, name='posting'),
    path('blog/new_post/', new_post, name='new_post'),
    path('blog/<int:pk>/remove/', remove_post, name='remove_post'),
]

# 이미지 URL 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
