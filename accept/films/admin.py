from django.contrib import admin

from .models import Actor
from .models import Address
from .models import Category
from .models import City
from .models import Country
from .models import Customer
from .models import Film
from .models import FilmActor
from .models import FilmCategory
from .models import Inventory
from .models import Language
from .models import Payment
from .models import Rental
from .models import Staff
from .models import Store


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("actor_id", "first_name", "last_name", "last_update")
    list_filter = ("last_update",)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        "address_id",
        "address",
        "address2",
        "district",
        "city",
        "postal_code",
        "phone",
        "last_update",
    )
    list_filter = ("last_update",)
    raw_id_fields = ("city",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_id", "name", "last_update")
    list_filter = ("last_update",)
    search_fields = ("name",)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("city_id", "city", "country", "last_update")
    list_filter = ("last_update",)
    raw_id_fields = ("country",)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("country_id", "country", "last_update")
    list_filter = ("last_update",)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "customer_id",
        "store",
        "first_name",
        "last_name",
        "email",
        "address",
        "activebool",
        "create_date",
        "last_update",
        "active",
    )
    list_filter = ("activebool", "create_date", "last_update")
    raw_id_fields = ("store", "address")


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = (
        "film_id",
        "title",
        "description",
        "release_year",
        "language",
        "original_language",
        "rental_duration",
        "rental_rate",
        "length",
        "replacement_cost",
        "rating",
        "last_update",
        "special_features",
        "fulltext",
    )
    list_filter = ("last_update",)
    raw_id_fields = ("language", "original_language")


@admin.register(FilmActor)
class FilmActorAdmin(admin.ModelAdmin):
    list_display = ("actor", "film", "last_update")
    list_filter = ("last_update",)
    raw_id_fields = ("actor", "film")


@admin.register(FilmCategory)
class FilmCategoryAdmin(admin.ModelAdmin):
    list_display = ("film", "category", "last_update")
    list_filter = ("last_update",)
    raw_id_fields = ("film", "category")


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ("inventory_id", "film", "store", "last_update")
    list_filter = ("last_update",)
    raw_id_fields = ("film", "store")


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("language_id", "name", "last_update")
    list_filter = ("last_update",)
    search_fields = ("name",)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "payment_id",
        "customer",
        "staff",
        "rental",
        "amount",
        "payment_date",
    )
    list_filter = ("payment_date",)
    raw_id_fields = ("customer", "staff", "rental")


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = (
        "rental_id",
        "rental_date",
        "inventory",
        "customer",
        "return_date",
        "staff",
        "last_update",
    )
    list_filter = ("rental_date", "return_date", "last_update")
    raw_id_fields = ("inventory", "customer", "staff")


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = (
        "staff_id",
        "first_name",
        "last_name",
        "address",
        "email",
        "store",
        "active",
        "username",
        "password",
        "last_update",
        "picture",
    )
    list_filter = ("address", "store", "active", "last_update")


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ("store_id", "manager_staff", "address", "last_update")
    list_filter = ("manager_staff", "address", "last_update")
