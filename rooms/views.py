from math import ceil
from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import models, forms
from django.views.generic import ListView, DetailView
from django.http import Http404
from django.shortcuts import render
from django_countries import countries
from django.urls import reverse

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

class RoomDetail(DetailView):

    """ RoomDetail Definition """
    template_name = 'rooms/detail.html'
    model = models.Room

def search(request):

    form = forms.SearchForm()

    return render(request, "rooms/search.html", {"form": form})