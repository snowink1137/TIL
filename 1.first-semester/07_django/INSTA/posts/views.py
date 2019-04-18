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
