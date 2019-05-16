# 20190516 django project on heroku

## 수업

### 준비

- 프로젝트 폴더 밖에 .git이 있으면 안된다!
  - 복사해와서 git init으로 .git 생성하고 venv 다시 설치하고 requirement.txt 통해서 library도 설치할 것.
- 추가적으로 `$ pip install whitenoise django-heroku gunicorn` 명령으로 위 library 들도 설치해줘야 함.



### 코드 수정

07_django/INSTA 에 있는 프로젝트를 복사해서 진행했다.

```python
# settings.py
# ...
import django_heroku
# ...
# SECRET_KEY = 'c!u&1c3ij6%e0q(^*nuh4gb_*w00up!_!--qtaua4jf$lg2&*v'
SECRET_KEY = os.environ.get('SECRET_KEY', 'c!u&1c3ij6%e0q(^*nuh4gb_*w00up!_!--qtaua4jf$lg2&*v')
# ...
# DEBUG = True
DEBUG = os.environ.get('DJANGO_DEBUG', True)
# ...
ALLOWED_HOSTS = ['*']
# ...
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
# ...
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
# ...
django_heroku.settings(locals())
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

```



이후에, `$ touch runtime.txt Procfile` 로 두 파일을 생성한다.

```markdown
# Procfile
release: python manage.py migrate
web: gunicorn insta.wsgi --log-file -
```

이때, 위의 insta 부분은 마스터 app 이름을 써주면 된다!

```markdown
# Procfile
release: python manage.py migrate
web: gunicorn <MY-MASTERAPP-NAME>.wsgi --log-file -
```

```markdown
# runtime.txt
python-3.7.3
```

그리고, 이제 파이참의 terminal을 쓰지 말고 따로 bash를 켜서 진행한다. 파이참의 terminal이 heroku를 못잡는다. 아마 환경 변수 문제인듯.

bash에서 `$ heroku login` 을 입력하고, 브라우저에서 로그인을 마무리한다.

그리고 bash를 하나 새로 켜고, `$ heroku create [프로젝트 이름]` 을 입력하면 heroku에 프로젝트가 등록되고, heroku의 git 주소와 연결된다.



