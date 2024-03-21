from rest_framework import viewsets

from accept.films.models import Actor
from accept.films.models import Address
from accept.films.models import Category
from accept.films.models import City
from accept.films.models import Country
from accept.films.models import Customer
from accept.films.models import Film
from accept.films.models import FilmActor
from accept.films.models import FilmCategory
from accept.films.models import Inventory
from accept.films.models import Language
from accept.films.models import Payment
from accept.films.models import Rental
from accept.films.models import Staff
from accept.films.models import Store

from .serializers import ActorSerializer
from .serializers import AddressSerializer
from .serializers import CategorySerializer
from .serializers import CitySerializer
from .serializers import CountrySerializer
from .serializers import CustomerSerializer
from .serializers import FilmActorSerializer
from .serializers import FilmCategorySerializer
from .serializers import FilmSerializer
from .serializers import InventorySerializer
from .serializers import LanguageSerializer
from .serializers import PaymentSerializer
from .serializers import RentalSerializer
from .serializers import StaffSerializer
from .serializers import StoreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    # no auth or premissions


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class FilmActorViewSet(viewsets.ModelViewSet):
    queryset = FilmActor.objects.all()
    serializer_class = FilmActorSerializer


class FilmCategoryViewSet(viewsets.ModelViewSet):
    queryset = FilmCategory.objects.all()
    serializer_class = FilmCategorySerializer


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
