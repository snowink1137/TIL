from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from .forms import CustomUserCreationForm, CustomUserAuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import User
from posts.forms import CommentModelForm


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)

        if form.is_valid():
            user = form.save()
            return redirect('posts:post_list')

    else:
        form = CustomUserCreationForm()

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
        form = CustomUserAuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            # DO LOGIN
            auth_login(request, user)
            messages.add_message(request, messages.SUCCESS, 'welcome back!')
            messages.add_message(request, messages.INFO, f'last login: {user.last_login}')

            return redirect(request.GET.get('next') or 'posts:post_list')
    # 사용자가 로그인 화면을 요청할 때
    else:
        form = CustomUserAuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@login_required
def logout(request):
    auth_logout(request)
    messages.add_message(request, messages.SUCCESS, '안녕히 가세요 :)')
    return redirect('posts:post_list')


def user_detail(request, username):
    user_info = User.objects.get(username=username)
    comment_form = CommentModelForm()

    context = {
        'user_info': user_info,
        'comment_form': comment_form,
    }

    return render(request, 'accounts/user_detail.html', context)


@login_required
@require_POST
def toggle_follow(request, username):
    sender = request.user
    receiver = get_object_or_404(User, username=username)

    if sender != receiver:
        if receiver in sender.followings.all():
            # unfollow
            sender.followings.remove(receiver)
        else:
            # follow
            sender.followings.add(receiver)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/insta/'))
