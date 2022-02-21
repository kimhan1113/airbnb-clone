from math import ceil
from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import models
from django.views.generic import ListView
from django.shortcuts import render

# Create your views here.

def all_rooms(request):
    page = request.GET.get("page", 1)
    if not page.isdecimal():
        return redirect("/?page=1")
    # page = int(page)
    # if not page is int:
    #     return redirect("/")
    # print(page)

    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)
    try:
        rooms = paginator.page(int(page))
        return render(request, "rooms/home.html", {"page": rooms})
    except EmptyPage:

        return redirect("/?page=1")


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created_at"
    context_object_name = "rooms"

def room_detail(request, pk):
    return render(request, "rooms/detail.html")