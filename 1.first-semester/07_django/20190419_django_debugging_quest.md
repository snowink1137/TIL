# 20190419 django debugging quest

## settings.py

- INSTALLED_APPS에 app 기록되어 있는지 확인

- ```python
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [os.path.join(BASE_DIR, 'practice', 'templates'), ],
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

- ```python
  MEDIA_URL = '/media/'
  MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
  ```

- ```python
  AUTH_USER_MODEL = 'auth.User'
  ```



## urls.py

- ```python
  from django.contrib import admin
  from django.urls import path, include
  
  # Media Upload
  from django.conf import settings
  from django.conf.urls.static import static
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('insta/', include('posts.urls')),
      path('accounts/', include('accounts.urls')),
  ]
  
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```

- ```python
  from . import views
  
  app_name = 'boards'
  ```



## models.py

- ```python
  from django.db import models
  from django_extensions.db.models import TimeStampedModel
  from imagekit.models import ProcessedImageField
  from imagekit.processors import ResizeToFill
  from django.conf import settings
  
  
  class Post(TimeStampedModel):
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      content = models.CharField(max_length=140)
      like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
  
  
  class Image(TimeStampedModel):
      post = models.ForeignKey(Post, on_delete=models.CASCADE)
      file = ProcessedImageField(
          blank=True,
          upload_to='posts/images',
          processors=[ResizeToFill(600, 600)],
          format='JPEG',
          options={'quality': 90}
      )
  
  
  class Comment(TimeStampedModel):
      content = models.CharField(max_length=100)
      post = models.ForeignKey(Post, on_delete=models.CASCADE)
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  ```



## views.py

### posts

- ```python
  from django.shortcuts import render, redirect, get_object_or_404
  from django.views.decorators.http import require_GET, require_POST, require_http_methods
  from django.contrib.auth.decorators import login_required
  from .models import Post, Image
  from .forms import PostModelForm, ImageModelForm, CommentModelForm
  
  
  @login_required
  @require_http_methods(['GET', 'POST'])
  def create_post(request):
      if request.method == 'POST':
          post_form = PostModelForm(request.POST)
  
          if post_form.is_valid():
              post = post_form.save(commit=False)
              post.user = request.user
              post.save()
              for image in request.FILES.getlist('file'):
                  request.FILES['file'] = image
                  image_form = ImageModelForm(files=request.FILES)
  
                  if image_form.is_valid():
                      image = image_form.save(commit=False)
                      image.post = post
                      image.save()
  
              return redirect('posts:post_list')
  
          else:
              pass
  
      else:
          post_form = PostModelForm()
  
      image_form = ImageModelForm()
      context = {
          'post_form': post_form,
          'image_form': image_form,
      }
  
      return render(request, 'posts/form.html', context)
  
  
  @require_http_methods(['GET', 'POST'])
  def update_post(request, post_id):
      post = get_object_or_404(Post, id=post_id)
      if post.user == request.user:
          if request.method == 'POST':
              form = PostModelForm(request.POST, instance=post)
              if form.is_valid():
                  form.save()
                  return redirect('posts:post_list')
  
          else:
              post_form = PostModelForm(instance=post)
  
          image_form = ImageModelForm()
          context = {
              'post_form': post_form,
              'image_form': image_form,
          }
          return render(request, 'posts/form.html', context)
      else:
          # 403 forbidden 금지됨!
          return redirect('posts:post_list')
  
  
  @require_GET
  def post_list(request):
      posts = Post.objects.all()
      comment_form = CommentModelForm()
  
      context = {
          'posts': posts,
          'comment_form': comment_form,
      }
  
      return render(request, 'posts/list.html', context)
  
  
  @login_required
  @require_POST
  def create_comment(request, post_id):
      post = get_object_or_404(Post, id=post_id)
      comment_form = CommentModelForm(data=request.POST)
  
      if comment_form.is_valid():
          comment = comment_form.save(commit=False)
          comment.user = request.user
          comment.post = post
          comment.save()
          return redirect('posts:post_list')
  
      # TODO else:
      # FIXME
  
  
  @login_required
  @require_POST
  def toggle_like(request, post_id):
      user = request.user
      post = get_object_or_404(Post, id=post_id)
  
      # if post.like_users.filter(id=user.id): # 찾으면, [value] / 없으면, []
      if user in post.like_users.all():
          post.like_users.remove(user)
      else:
          post.like_users.add(user)
  
      return redirect('posts:post_list')
  
  ```



### account

- ```python
  from django.shortcuts import render, redirect
  from django.views.decorators.http import require_http_methods, require_GET, require_POST
  from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
  from django.contrib.auth import login as auth_login, logout as auth_logout
  
  
  @require_http_methods(['GET', 'POST'])
  def signup(request):
      if request.method == 'POST':
          form = UserCreationForm(data=request.POST)
  
          if form.is_valid():
              user = form.save()
              return redirect('posts:post_list')
  
      else:
          form = UserCreationForm()
  
      context = {
          'form': form,
      }
      return render(request, 'accounts/signup.html', context)
  
  
  @require_http_methods(['GET', 'POST'])
  def login(request):
      # 우선, 사용자가 로그인 되어 있는지?
      if request.user.is_authenticated:
          return redirect('posts:post_list')
  
      # 사용자가 로그인 데이터를 넘겼을 때
      if request.method == 'POST':
          form = AuthenticationForm(request, data=request.POST)
  
          if form.is_valid():
              # DO LOGIN
              auth_login(request, form.get_user())
  
              return redirect(request.GET.get('next') or 'posts:post_list')
      # 사용자가 로그인 화면을 요청할 때
      else:
          form = AuthenticationForm()
  
      context = {
          'form': form,
      }
      return render(request, 'accounts/login.html', context)
  
  
  def logout(request):
      auth_logout(request)
      return redirect('posts:post_list')
  
  ```



## html

### base.html

- ```python
  {% if user.is_authenticated %}
      <li class="nav-item">
      	<a class="nav-link" href="{% url 'posts:create_post' %}">New</a>
      </li>
      <li class="nav-item">
      	<a class="nav-link" href="#">{{ user.username }}</a>
      </li>
      <li class="nav-item">
      	<a class="nav-link" href="{% url 'accounts:logout' %}">Logout</a>
      </li>
  {% else %}
      <li class="nav-item">
      	<a class="nav-link" href="{% url 'accounts:login' %}">Login</a>
      </li>
      <li class="nav-item">
      	<a class="nav-link" href="{% url 'accounts:signup' %}">Signup</a>
      </li>
  {% endif %}
  ```



### form.html

- ```python
  {% extends 'base.html' %}
  {% load bootstrap4 %}
  
  {% block body %}
      <h1>New post</h1>
      <form method="POST" enctype="multipart/form-data">
          {% csrf_token %}
          {% bootstrap_form post_form %}
          {% if image_form %}
              {% bootstrap_form image_form %}
          {% endif %}
          {% buttons %}
              <button type="submit" class="btn btn-primary">Submit</button>
          {% endbuttons %}
      </form>
  {% endblock %}
  ```



### _post.html

- ```python
  {% load bootstrap4 %}
  <div class="card my-3">
      {% if post.image_set %}
          <div id="post{{post.id}}" class="carousel slide carousel-fade" data-ride="carousel">
              <div class="carousel-inner">
                  {% for image in post.image_set.all %}
                      <div class="carousel-item {% if forloop.counter == 1 %} active {% endif %}">
                          <img src="{{ image.file.url }}" class="d-block w-100" alt="{{ image.file }}">
                      </div>
                  {% endfor %}
              </div>
              <a class="carousel-control-prev" href="#post{{post.id}}" role="button" data-slide="prev">
                  <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                  <span class="sr-only">Previous</span>
              </a>
              <a class="carousel-control-next" href="#post{{post.id}}" role="button" data-slide="next">
                  <span class="carousel-control-next-icon" aria-hidden="true"></span>
                  <span class="sr-only">Next</span>
              </a>
          </div>
      {% else %}
          <img src="https://picsum.photos/600" alt="random-image" class="card-img-top" />
      {% endif %}
      <div class="card-body">
          <p class="card-text">posted by {{ post.user }}</p>
          <p class="card-text">{{post.content}}</p>
          {% if user == post.user %}
          <a href="{% url 'posts:update_post' post.id %}" class="btn btn-warning">수정</a>
          {% endif %}
      </div>
  
      <div class="card-body">
          <form action="{% url 'posts:toggle_like' post_id=post.id %}" method="POST">
              {% csrf_token %}
              {% if user in post.like_users.all %}
                  <span>총 좋아요 수:</span> <span>{{ post.like_users.all.count }}</span>
                  <button type="submit" class="btn btn-danger">좋아요 취소</button>
              {% else %}
                  <span>총 좋아요 수:</span> <span>{{ post.like_users.all.count }}</span>
                  <button type="submit" class="btn btn-info">좋아요</button>
              {% endif %}
          </form>
      </div>
  
  
      <div class="card-body">
              {% for comment in post.comment_set.all %}
                  <p class="card-text">
                      <strong>{{ comment.user.username }}</strong>: {{ comment.content }}
                  </p>
              {% empty %}
                  <p class="card-text">
                      댓글을 달아주세요!
                  </p>
              {% endfor %}
  
      </div>
      <div class="card-footer">
          <form action="{% url 'posts:create_comment' post_id=post.id %}" method="POST">
              {% csrf_token %}
              {{ comment_form.content }}
              <input type="submit" class="btn btn-light">
          </form>
      </div>
  </div>
  ```



### list.html

- ```python
  {% extends 'base.html' %}
  
  {% block body %}
      <h1>Posts</h1>
      <section class="card-columns">
          {% for post in posts %}
              {% include 'posts/_post.html' with post=post comment_form=comment_form %}
          {% endfor %}
      </section>
  
  {% endblock %}
  ```



## admin.py

- ```python
  from django.contrib import admin
  from .models import Post
  
  
  class PostModelAdmin(admin.ModelAdmin):
      readonly_fields = ('created', 'modified')
      list_display = ('id', 'content', 'created', 'modified')
      list_display_links = ('id', 'content')
  
  
  admin.site.register(Post, PostModelAdmin)
  
  ```





