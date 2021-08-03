# django month test summary

- ```python
  # settings.py
  ALLOWED_HOSTS = ['*']
  AUTH_USER_MODEL = 'auth.User'
  ```

- ```python
  # account/views.py
  
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
      if request.user.is_authenticated:
          return redirect('posts:posts')
          
      if request.method == 'POST':
          form = UserAuthenticationForm(request, data=request.POST)
          
          if form.is_valid():
              user = form.get_user()
              auth_login(request, user)
              
              return redirect('posts:post_list')
              
      else:
          form = UserAuthenticationForm()
          
      context = {
          'form': form,
      }
      
      return render(request, 'accounts/login.html', context)
  
  
  ```

- 