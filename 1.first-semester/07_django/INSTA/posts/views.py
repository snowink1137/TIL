from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Image, HashTag
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

            # create hashtag => <input name='tags' /> #hi #ssafy #20층
            content = post_form.cleaned_data.get('content')  #
            words = content.split(' ')  # 띄어쓰기 기준으로 split
            for word in words:
                if word[0] == '#':
                    word = word[1:]
                    tag = HashTag.objects.get_or_create(content=word)  # (HashTag 객체, 생성 여부) 이런식으로 반환됨.
                    post.tags.add(tag[0])
                    if tag[1]:  # 태그가 처음 만들어진거라면
                        messages.add_message(request, messages.SUCCESS, f'{tag[0].content} 태그를 처음으로 추가하셨어요!')

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
            post_form = PostModelForm(request.POST, instance=post)
            if post_form.is_valid():
                post_form.save()

                # update hashtag
                post.tags.clear()  # 기존의 tag 다 날리기

                content = post_form.cleaned_data.get('content')  #
                words = content.split(' ')  # 띄어쓰기 기준으로 split
                for word in words:
                    if word[0] == '#':
                        word = word[1:]
                        tag = HashTag.objects.get_or_create(content=word)  # (HashTag 객체, 생성 여부) 이런식으로 반환됨.
                        post.tags.add(tag[0])

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
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/insta/'))

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


@require_GET
def tag_posts_list(request, tag_name):
    tag = get_object_or_404(HashTag, content=tag_name)
    posts = tag.posts.all()
    comment_form = CommentModelForm()

    context = {
        'posts': posts,
        'comment_form': comment_form,
        'h1': f'#{tag}를 포함한 posts 입니다.',
    }

    return render(request, 'posts/list.html', context)
