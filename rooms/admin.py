from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin
from django.utils.safestring import mark_safe

from rooms.models import Room, RoomType, Facility, Amenity, HouseRule, Photo


@admin.register(RoomType, Facility, Amenity, HouseRule)
class ItemAdmin(ModelAdmin):

    list_display = [
        "name",
        "used_by"
    ]

    def used_by(self, obj):
        return obj.rooms.count()

class PhotoInline(admin.TabularInline):

# class PhotoInline(admin.StackedInline):
# 위에꺼랑 layout만다르다!
    model = Photo

@admin.register(Room)
class RoomAdmin(ModelAdmin):
    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic Info",
            {"fields" : ("name", "description", "country", "address", "price")},
        ),
        (
            "Times",
            {"fields": ("check_in", "check_out", "instant_book")},
        ),
        (
          "Space",
          {"fields": ("guests", "beds", "bedrooms", "baths")},
        ),
        (
          "More About the Space",

          {
              # "classes": ("collapse",),
              "fields": ("amenities","facilities","house_rules"),
          },
        ),
        (
          "Last Detail",
          {"fields": ("host",)},
        ),

    )



    # manytomany필드는 여기에 넣을 수 없다.
    list_display = [
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    ]

    list_filter = [
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    ]

    raw_id_fields = ("host",)

    search_fields = ["city","^host__username"]

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )


    # @admin.display(empty_value='unknown')
    # def amenities_view(self, obj):
    #      return obj.amenities

    def count_amenities(self, obj):
        # print(obj)
        # print(obj.amenities.all().count())
        # print(obj.amenities.all())
        return obj.amenities.count()

    def count_photos(self, obj):

        return obj.photos.count()

    count_photos.short_description = "Photo Count"
    # 컬럼명을 바꿔줄 수 있음!
    # count_amenities.short_description = "hello sexy!~"


@admin.register(Photo)
class PhotoAdmin(ModelAdmin):
    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"