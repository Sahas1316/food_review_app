from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
from foodreview.models import Menu, Comment

# Create your views here.
def index(request):
    context = {
        "menus": Menu.objects.all()
    }
    return render(request, 'foodreview/index.html', context)

def detail(request, menu_id):
    try:
        menu = Menu.objects.get(pk=menu_id)
    except Menu.DoesNotExist:
        raise Http404("Menu does not exist")

    if request.method == 'POST':
        comment = Comment(menu=menu, text=request.POST['text'])
        comment.save()

    context = {
        "menu": menu,
        'comments': menu.comments.order_by('-posted_at')
    }
    return render(request, "foodreview/detail.html", context)

def create(request):
    if request.method == 'POST':
        menu = Menu(menu=request.POST['menu'], description=request.POST['description'], price=request.POST['price'], image=request.FILES['img'])
        menu.save()
        context = {
            "menu": menu,
        }
        return render(request, 'foodreview/detail.html', context)
    else:
        return render(request, 'foodreview/create.html')

def like(request, menu_id):
    try:
        menu = Menu.objects.get(pk=menu_id)
        menu.like += 1
        menu.save()
    except Menu.DoesNotExist:
        raise Http404("Article does not exist")
    return redirect(detail, menu_id)

def delete(request, menu_id):
    try:
        menu = Menu.objects.get(pk=menu_id)
    except Menu.DoesNotExist:
        raise Http404("Menu does not exist")
    menu.delete()
    return redirect(index)
def edit(request, menu_id):
    try:
        menu = Menu.objects.get(pk=menu_id)
    except Menu.DoesNotExist:
        raise Http404("Menu does not exist")
    if request.method == 'POST':
        menu.menu = request.POST['menu']
        menu.description = request.POST['description']
        menu.price = request.POST['price']
        menu.save()
        return redirect(detail, menu_id)
    context = {
        "menu": menu
    }
    return render (request, "foodreview/edit.html", context)

def map(request):
    return render (request, "foodreview/map.html")
