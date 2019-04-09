from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Posting, Comment
from django.views.decorators.http import require_http_methods


# Create
def create_posting(request):
    if request.method == 'POST':
        posting = Posting()
        posting.title = request.POST.get('title')
        posting.content = request.POST.get('content')
        posting.save()

        return redirect('board_ad:posting_detail', posting_id=posting.id)

    elif request.method == 'GET':
        return render(request, 'board_ad/new.html')


# Read
def posting_list(request):
    postings = Posting.objects.all()
    # postings = get_list_or_404(Posting)  # 얘는 404를 띄우므로 적절하지 않다.

    context = {
        'postings': postings,
    }

    return render(request, 'board_ad/list.html', context)


def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comments = posting.comment_set.all()

    context = {
        'posting': posting,
        'comments': comments,
    }

    return render(request, 'board_ad/detail.html', context)


# Update
def update_posting(request, posting_id):
    if request.method == 'POST':
        posting = get_object_or_404(Posting, id=posting_id)
        posting.title = request.POST.get('title')
        posting.content = request.POST.get('content')
        posting.save()

        return redirect('board_ad:posting_detail', posting_id=posting_id)

    elif request.method == 'GET':
        posting = get_object_or_404(Posting, id=posting_id)
        context = {
            'posting': posting,
        }

        return render(request, 'board_ad/edit.html', context)


# Delete
@require_http_methods(['POST'])
def delete_posting(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    posting.delete()

    return redirect('board_ad:posting_list')


@require_http_methods(['POST'])
def create_comment(request, posting_id):
    comment = Comment()
    posting = get_object_or_404(Posting, id=posting_id)
    comment.posting = posting
    comment.content = request.POST.get('content')
    comment.save()

    return redirect('board_ad:posting_detail', posting_id)


@require_http_methods(['POST'])
def delete_comment(request, posting_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()

    return redirect('board_ad:posting_detail', posting_id)
