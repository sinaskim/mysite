"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin #django.contrib에서 admin을 불러온다.
from django.urls import path #django.urls에서 path를 불러온다.
import blog.views # blog의 views를 불러온다.
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('base/', blog.views.base, name='base'), #사이트 경로 지정  
    path('', blog.views.main, name='main'), #''은 사이트를 먼저 켰을때, 제일 먼저 뜨는 페이지로 설정. 이름은 main으로 정한다.
    path('write/create/', blog.views.create, name='create'), #write/create로 경로지정을하고 이름은 create로 정한다.
    path('edit/<str:id>/', blog.views.edit, name='edit'), #edit와 문자열 id를받아 경로를 지정하고 이름은 edit으로 정한다.
    path('detail/<str:id>/', blog.views.detail, name='detail'), #detail과 문자열 id를받아 경로를 지정하고 이름은 detail으로 정한다.
    path('delete/<str:id>/', blog.views.delete, name='delete'), #delete와 문자열 id를받아 경로를 지정하고 이름은 delete으로 정한다.
    path('hashtag/', blog.views.hashtagform, name='hashtag'),
    path('<int:hashtag_id>/search/',blog.views.search, name ='search'),
    path('account/', include('account.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
