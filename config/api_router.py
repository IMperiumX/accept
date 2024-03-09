from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from accept.films.api.views import ActorViewSet
from accept.films.api.views import AddressViewSet
from accept.films.api.views import CategoryViewSet
from accept.films.api.views import CityViewSet
from accept.films.api.views import CountryViewSet
from accept.films.api.views import CustomerViewSet
from accept.films.api.views import FilmActorViewSet
from accept.films.api.views import FilmCategoryViewSet
from accept.films.api.views import FilmViewSet
from accept.films.api.views import InventoryViewSet
from accept.films.api.views import LanguageViewSet
from accept.films.api.views import PaymentViewSet
from accept.films.api.views import RentalViewSet
from accept.films.api.views import StaffViewSet
from accept.films.api.views import StoreViewSet
from accept.users.api.views import UserViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register("actors", ActorViewSet)
router.register("addresses", AddressViewSet)
router.register("categories", CategoryViewSet)
router.register("cities", CityViewSet)
router.register("countries", CountryViewSet)
router.register("customers", CustomerViewSet)
router.register("films", FilmViewSet)
router.register("film-actors", FilmActorViewSet)
router.register("film-categories", FilmCategoryViewSet)
router.register("inventories", InventoryViewSet)
router.register("languages", LanguageViewSet)
router.register("payments", PaymentViewSet)
router.register("rentals", RentalViewSet)
router.register("staff", StaffViewSet)
router.register("stores", StoreViewSet)

app_name = "api"
urlpatterns = router.urls
