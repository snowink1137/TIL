# 20190123 sql django

## 수업

### db

- c9/django-basic/sqlite 에서 sqlite3로 sql 연습함.
  - timetables.sql
- codecademy.com sql 3단계까지 하기.
  - 맨 끝에 정리 괜찮음.
  - join 계속 헷갈리는데 gif 괜찮다.

- table의 ER 시각화해주는 사이트 : http://aquerytool.com/



### django

- framework

  - 카페 차릴 때 프랜차이즈 같은 것
  - frame 이외의 일을 하기는 어렵지만 장점이 많다.
  - 하지만 너무 다양해서 사실상 제한 없음.

- MTV

  - 다른 프레임워크의 MVC 패턴과 거의 비슷한데 다른 이름으로 쓰는 것임.
  - Model, Template, View
    - Template가 다른 프레임워크의 view이고, View가 다른 프레임워크의 controller인 듯 하다.

- 시작

  - `$ django-admin startproject '프로젝트명'`

  - `$ python manage.py runserver $IP:$PORT`

    - 명령어 안에 쓰이는 $의 의미 : 환경 변수를 얘기하는 것.
    - 예전에 export FLASK_ENV = 'production' 이 명령어로 환경 변수 지정한 것처럼 미리 지정되어 있는 환경변수 IP와 PORT 불러오는 것임.

  - setting.py 에서 ALLOWED_HOST 리스트에 우리 주소 지정 해줘야 함.

    - ```python
      ALLOWED_HOSTS = [
          'django-basic-snowink1137-1.c9users.io',    
      ]
      ```

    - 이런식으로 https:// 떼고, 맨뒤에 /도 떼야 함.

    - 리스트 끝에 ',' 넣어 주는 게 

  - django는 app들의 집합으로 이루어진 project라고 생각하면 됨.

    - project 이름과 같은 first_django 폴더는 최상단 app이다.

  - app 만들기

    - `$ django-admin startapp home`

    - 프로젝트 폴더 안에 새로운 폴더 생김.

    - 만들고 난 후 최상단 app 안의 setting.py에 등록 해줘야 함. 이런식으로.

    - ```python
      INSTALLED_APPS = [
          'django.contrib.admin',
          'django.contrib.auth',
          'django.contrib.contenttypes',
          'django.contrib.sessions',
          'django.contrib.messages',
          'django.contrib.staticfiles',
          'home',
      ]
      ```

  - app 다루기

    - flask와 다르게 django 데코레이터 대신에 routing은 최상위 app의 urls.py에 설정해줘야함.

    - ```python
      urlpatterns = [
          path('admin/', admin.site.urls),
          path('', views.index),
          path('lotto/', views.lotto),
      ]
      ```

  - templete 설정

    - templete 폴더를 만들고 그 주소를 settings.py에 등록해줘야함

    - ```python
      import os
      
      # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
      BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
      TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
      ```

    - ```python
      TEMPLATES = [
          {
              'BACKEND': 'django.template.backends.django.DjangoTemplates',
              'DIRS': [TEMPLATES_DIR],
              'APP_DIRS': True,
              'OPTIONS': {
                  'context_processors': [
                      'django.template.context_processors.debug',
                      'django.template.context_processors.request',
                      'django.contrib.auth.context_processors.auth',
                      'django.contrib.messages.context_processors.messages',
                  ],
              },
          },
      ]
      ```

    - 이런식으로 수정!





## 수업 이외

