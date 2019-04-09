from django.shortcuts import render, redirect
from .models import Posting


def posting_list(request):
    postings = Posting.objects.all()

    context = {
        'postings': postings,
    }

    return render(request, 'board_ad/list.html', context)


def posting_detail(request, id):
    posting = Posting.objects.get(id=id)

    context = {
        'posting': posting,
    }

    return render(request, 'board_ad/detail.html', context)
