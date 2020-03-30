from django.shortcuts import render, redirect
from .forms import *



def create(request):
    if request.method == 'POST':
        form = WriterModelForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('detail')
        else:
            pass

    elif request.method == 'GET':
        form = WriterModelForm()

    context = {
        'form': form,
    }

    return render(request, 'new.html', context)


def update(request, id):
    writer = Writer.objects.get(id=id)

    if request.method == 'POST':
        form = WriterModelForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('성공!')
        else:
            return redirect('실패!')

    elif request.method == 'GET':
        form = WriterModelForm(instance=writer)
        context = {
            'form': form,
        }

        return render(request, 'edit.html', context)

