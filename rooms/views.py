from math import ceil
from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import models, forms
from django.views.generic import ListView, DetailView, View
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
    paginate_by = 12
    paginate_orphans = 5
    ordering = "created_at"
    context_object_name = "rooms"

class RoomDetail(DetailView):

    """ RoomDetail Definition """
    template_name = 'rooms/detail.html'
    model = models.Room

class SearchView(View):

    def get(self, request):
        country = request.GET.get("country")

        if country:

            form = forms.SearchForm(request.GET)

            if form.is_valid():

                city = form.cleaned_data.get("city")
                country = form.cleaned_data.get("country")
                room_type = form.cleaned_data.get("room_type")
                price = form.cleaned_data.get("price")
                guests = form.cleaned_data.get("guests")
                bedrooms = form.cleaned_data.get("bedrooms")
                beds = form.cleaned_data.get("beds")
                baths = form.cleaned_data.get("baths")
                instant_book = form.cleaned_data.get("instant_book")
                superhost = form.cleaned_data.get("superhost")
                amenities = form.cleaned_data.get("amenities")
                facilities = form.cleaned_data.get("facilities")

                filter_args = {}

                if city != "Anywhere":
                    filter_args["city__startswith"] = city

                filter_args["country"] = country

                if room_type is not None:
                    filter_args["room_type"] = room_type

                if price is not None:
                    filter_args["price__lte"] = price

                if guests is not None:
                    filter_args["guests__gte"] = guests

                if bedrooms is not None:
                    filter_args["bedrooms__gte"] = bedrooms

                if beds is not None:
                    filter_args["beds__gte"] = beds

                if baths is not None:
                    filter_args["baths__gte"] = baths

                if instant_book is True:
                    filter_args["instant_book"] = True

                if superhost is True:
                    filter_args["host__superhost"] = True

                for amenity in amenities:
                    filter_args["amenities"] = amenity

                for facility in facilities:
                    filter_args["facilities"] = facility

                qs = models.Room.objects.filter(**filter_args).order_by("-created_at")

                paginator = Paginator(qs, 10, orphans=5)

                page = request.GET.get("page", 1)

                rooms = paginator.get_page(page)

                return render(
                    request, "rooms/search.html", {"form": form, "rooms": rooms}
                )

        else:

            form = forms.SearchForm()

        return render(request, "rooms/search.html", {"form": form})
