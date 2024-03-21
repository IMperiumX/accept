from django.db import models


class Actor(models.Model):
    actor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    last_update = models.DateTimeField()

    class Meta:
        db_table = "actor"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, blank=True, default="")
    district = models.CharField(max_length=20)
    city = models.ForeignKey("City", models.DO_NOTHING)
    postal_code = models.CharField(max_length=10, blank=True, default="")
    phone = models.CharField(max_length=20)
    last_update = models.DateTimeField()

    class Meta:
        db_table = "address"

    def __str__(self):
        return f"{self.address} - {self.city}"


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    last_update = models.DateTimeField()

    class Meta:
        db_table = "category"

    def __str__(self):
        return f"{self.name}"


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=50)
    country = models.ForeignKey("Country", models.DO_NOTHING)
    last_update = models.DateTimeField()

    class Meta:
        db_table = "city"

    def __str__(self):
        return f"#{self.city_id} {self.city}"


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=50)
    last_update = models.DateTimeField()

    class Meta:
        db_table = "country"

    def __str__(self):
        return f"{self.country}"


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    store = models.ForeignKey("Store", models.DO_NOTHING)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=50, blank=True, default="")
    address = models.ForeignKey(Address, models.DO_NOTHING)
    activebool = models.BooleanField()
    create_date = models.DateField()
    last_update = models.DateTimeField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = "customer"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Film(models.Model):
    film_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_year = models.IntegerField(blank=True, null=True)
    language = models.ForeignKey("Language", models.DO_NOTHING)
    original_language = models.ForeignKey(
        "Language",
        models.DO_NOTHING,
        related_name="film_original_language_set",
        blank=True,
        null=True,
    )
    rental_duration = models.SmallIntegerField()
    rental_rate = models.DecimalField(max_digits=4, decimal_places=2)
    length = models.SmallIntegerField(blank=True, null=True)
    replacement_cost = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.TextField()
    last_update = models.DateTimeField()
    special_features = models.TextField()
    fulltext = models.TextField()

    class Meta:
        db_table = "film"

    def __str__(self):
        return f"{self.title}"


class FilmActor(models.Model):
    actor = models.OneToOneField(
        Actor,
        models.DO_NOTHING,
        primary_key=True,
    )
    film = models.ForeignKey(Film, models.DO_NOTHING)
    last_update = models.DateTimeField()

    class Meta:
        db_table = "film_actor"
        unique_together = (("actor", "film"),)

    def __str__(self):
        return f"{self.actor} - {self.film}"


class FilmCategory(models.Model):
    film = models.OneToOneField(
        Film,
        models.DO_NOTHING,
        primary_key=True,
    )
    category = models.ForeignKey(Category, models.DO_NOTHING)
    last_update = models.DateTimeField()

    class Meta:
        db_table = "film_category"
        unique_together = (("film", "category"),)

    def __str__(self):
        return f"{self.film} - {self.category}"


class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    film = models.ForeignKey(Film, models.DO_NOTHING)
    store = models.ForeignKey("Store", models.DO_NOTHING)
    last_update = models.DateTimeField()

    class Meta:
        db_table = "inventory"

    def __str__(self):
        return f"{self.film} - {self.store}"


class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    name = models.CharField()
    last_update = models.DateTimeField()

    class Meta:
        db_table = "language"

    def __str__(self):
        return f"{self.name}"


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    staff = models.ForeignKey("Staff", models.DO_NOTHING)
    rental = models.ForeignKey("Rental", models.DO_NOTHING)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    payment_date = models.DateTimeField()

    class Meta:
        db_table = "payment"

    def __str__(self):
        return f"{self.customer} - {self.amount}"


class Rental(models.Model):
    rental_id = models.AutoField(primary_key=True)
    rental_date = models.DateTimeField()
    inventory = models.ForeignKey(Inventory, models.DO_NOTHING)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    return_date = models.DateTimeField(blank=True, null=True)
    staff = models.ForeignKey("Staff", models.DO_NOTHING)
    last_update = models.DateTimeField()

    class Meta:
        db_table = "rental"
        unique_together = (("rental_date", "inventory", "customer"),)

    def __str__(self):
        return f"{self.rental_date} - {self.inventory} - {self.customer}"


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    address = models.ForeignKey(Address, models.DO_NOTHING)
    email = models.CharField(max_length=50, default="")
    store = models.ForeignKey("Store", models.DO_NOTHING)
    active = models.BooleanField()
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=40, default="")
    last_update = models.DateTimeField()
    picture = models.BinaryField(blank=True, null=True)

    class Meta:
        db_table = "staff"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    manager_staff = models.OneToOneField(
        Staff,
        models.DO_NOTHING,
        related_name="stores",
    )
    address = models.ForeignKey(Address, models.DO_NOTHING)
    last_update = models.DateTimeField()

    class Meta:
        db_table = "store"

    def __str__(self):
        return f"{self.store_id}"
