# 20190412

## 수업

### REST

- REST란?
  - Representational State Transfer의 약자
  - 즉, 자원(resource)의 표현(representation) 에 의한 상태 전달
  - 월드 와이드 웹(www)과 같은 분산 하이퍼미디어 시스템을 위한 소프트웨어 개발 아키텍처의 한 형식
    - REST는 기본적으로 웹의 기존 기술과 HTTP 프로토콜을 그대로 활용하기 때문에 웹의 장점을 최대한 활용할 수 있는 아키텍처 스타일이다.
    - REST는 네트워크 상에서 Client와 Server 사이의 통신 방식 중 하나이다.
  - REST의 구체적인 개념
    - HTTP URI(Uniform Resource Identifier)를 통해 자원(Resource)을 명시하고, HTTP Method(POST, GET, PUT, DELETE)를 통해 해당 자원에 대한 CRUD Operation을 적용하는 것을 의미한다.
  - (ex)
    - `GET /articles/1`: 1번 조회
    - `GET /articles/`: 전체 조회
    - `GET /articles/1/edit`: 1번 수정하는 페이지
    - `PATCH /articles/1`: 1번 수정
    - `DELETE /articles/1`: 1번 삭제
    - `GET /articles/new`: 새로 데이터 입력하는 페이지
    - `POST /articles/`: 새로 article 생성

- RESTful이란?
  - RESTful은 일반적으로 REST라는 아키텍처를 구현하는 웹 서비스를 나타내기 위해 사용되는 용어이다.
  - ‘REST API’를 제공하는 웹 서비스를 ‘RESTful’하다고 할 수 있다.

- REST가 등장한 이유?
  - 애플리케이션 분리 및 통합
  - 다양한 클라이언트의 등장
- REST 구성 요소
  - 자원(Resource): URI
    - 모든 자원에 고유한 ID가 존재하고, 이 자원은 Server에 존재한다.
  - 행위(Verb): HTTP Method
    - HTTP 프로토콜의 Method를 사용한다.(GET, POST, PUT(PATCH), DELETE)
  - 표현(Representation of Resource)
    - Client가 자원에 대해 요청하면 Server는 이에 응답한다.
    - 보통은 JSON, XML 형태의 자원을 주고 받는다.

- [출처] https://gmlwjd9405.github.io/2018/09/21/rest-and-restful.html



### django-rest-framework 모듈

- django에서 REST를 구현하는 것을 도와주는 모듈

- Response, api_view를 통해 기존의 render 및 redirect 같은 것을 대체할 수 있고, serializer를 활용하면 API도 쉽게 구현할 수 있다. 구현은 `forms.py`를 만들었던 것과 비슷하다.

- ```python
  # serializers.py
  
  from rest_framework import serializers
  from .models import Movie
  
  
  class MovieSerializer(serializers.ModelSerializer):
      class Meta:
          model = Movie
          fields = '__all__'
  
  ```

- ```python
  # views.py
  
  from django.shortcuts import get_list_or_404, get_object_or_404
  from rest_framework.decorators import api_view
  from rest_framework.response import Response
  from .models import Movie
  from .serializers import MovieSerializer
  
  
  @api_view(['GET'])
  def movie_list(request):
      movies = get_list_or_404(Movie)
      serializer = MovieSerializer(movies, many=True)
  
      return Response(serializer.data)
  
  
  @api_view(['GET', 'PATCH', 'DELETE'])
  def one_movie(request, movie_id):
      movie = get_object_or_404(Movie, id=movie_id)
  
      if request.method == 'GET':
          serializer = MovieSerializer(movie)
          return Response(serializer.data)
      elif request.method == 'PATCH':
          serializer = MovieSerializer(data=request.data, instance=movie)
          if serializer.is_valid(raise_exception=True):
              serializer.save()
              return Response({'message': 'Movie Edited!'})
      else:
          movie.delete()
          return Response({'message': 'Movie Deleted!'})
  
  
  @api_view(['POST'])
  def create_movie(request):
      serializer = MovieSerializer(data=request.data)
  
      if serializer.is_valid(raise_exception=True):
          serializer.save()
          return Response(serializer.data)
  
  ```

- `postman`프로그램으로 GET, POST 등의 요청을 쉽게 보낼 수 있다. 이를 통해 API가 제대로 작동하는지 알아보면 된다.



### 직렬화(serialize)

- 이거 보고 써놓기.

- [출처] https://okky.kr/article/224715
- [출처] http://woowabros.github.io/experience/2017/10/17/java-serialize.html





### faker 모듈

- dummy 데이터를 만들어주는 모듈이다. 파이썬말고 다른 언어에도 있는 모듈인 듯하다.

- ```python
  # model.py
  
  from django.db import models
  from faker import Faker
  
  faker = Faker()
  
  
  class Movie(models.Model):
      title = models.CharField(max_length=100)
  
      @classmethod
      def dummy(cls, n):
          for _ in range(n):
              cls.objects.create(
                  title=faker.catch_phrase(20)
              )
  
  ```

- Movie 클래스가 `model.Model`을 상속했기 때문에 `cls.objects.create`와 같은 메소드가 존재하는 것 같다.



## 수업 외



