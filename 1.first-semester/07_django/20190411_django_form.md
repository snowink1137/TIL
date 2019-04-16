# 20190411 django form

## 수업

### form

- 기존 CRUD 구현에 form을 활용하여 좀더 편하고 효과적으로 서버를 만들 수 있음!

- django ORM(`Model.py`)인 models 모듈로 데이터베이스 관련한 작업을 편하게 django에서 처리했던 것처럼, forms 모듈을 `forms.py`에 구현하여 사용자가 form으로 받는 작업을 편하게 할 수 있다.

- (ex)

  - 예를 들면, 내가 구성한 model에 맞게 form 입력 양식을 html로 구현이 편하다. front쪽 일 편하게.
  - 사용자로부터 받은 form 정보에 대한 유효성 검증이 편하다. back쪽 일 편하게.

- forms 모듈 구현 방법 1(`forms.py`)

  - 기존에 만들어 두었던 model을 바탕으로 form 양식을 구성하는 것이다. 따라서, model 정보가 필요하므로 필요한 model을 import한다.

  - ```python
    from django import forms
    from .models import Post
    
    
    class PostModelForm(forms.ModelForm):
        class Meta:
            model = Post
            fields = '__all__'
    ```

  - 내부 클래스 Meta는 이 Form이 어떤 model을 기반으로 만들어졌는지, 어떤 field를 대상으로 할 것인지 지정하는 클래스이다.

- forms 모듈 구현 방법 2(`views.py`)

  - ```python
    from .forms import PostModelForm
    
    
    @require_http_methods(['GET', 'POST'])
    def create_post(request):
        # POST 방식으로 넘온 Data 를 ModelForm 에 넣는다.
        if request.method == 'POST':
            # POST 방식으로 넘온 Data 를 ModelForm 에 넣는다.
            form = PostModelForm(request.POST, request.FILES)
    
            # Data 검증을 한다.
            if form.is_valid():
                # 통과하면 저장한다.
                form.save()
    
                return redirect('posts:post_list')
            else:
    
                # 실패하면, 다시 data 입력 form 을 준다.
                pass
    
        # GET 방식으로 요청이 오면,
        else:
            form = PostModelForm()
    
        return render(request, 'posts/form.html', {
            'form': form,
        })
    ```

  - `forms.py`에서 만들어 놓았던 클래스를 import해서 사용한다.

  - `ModelForm`을 상속받아서 만든 클래스이기 때문에 `is_valid`같은 유용한 메소드를 사용할 수 있다.

- forms 모듈 구현 방법 3(`form.html`)

  - ```html
    {% extends 'base.html' %}
    {% load bootstrap4 %}
    
    {% block body %}
        <h1>New post</h1>
        <form method="POST" enctype="multipart/form-data">
            {% csrf_token %}
            {% bootstrap_form form %}
            {% buttons %}
                <button type="submit" class="btn btn-primary">Submit</button>
            {% endbuttons %}
        </form>
    {% endblock %}
    ```

  - 이런 식으로 `view.py`에서 넘어온 `form`은 html에서 알아서 구현된다. 위의 예제는 `form`에 django-bootstrap을 추가적으로 사용했다.



### django-bootstrap

- django 프레임워크에서 bootstrap이 적용할 수 있도록 해주는 모듈이다.
- 위에 `form 모듈 구현 방법 3`에 그 예시가 써 있다.



### ORM으로 file 저장

- `settings.py`에 MEDIA 옵션을 추가해준다.

  - ```python
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    ```

- html 문서 form 태그에 enctype 옵션을 추가해줘야 한다.

  - `<form method="POST" enctype="multipart/form-data">`

- 데이터베이스에 file을 직접 저장하는 것이 아니라 file은 media에 저장하고 데이터베이스에는 이름만 저장하는 것.



## 수업 이외

