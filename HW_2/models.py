from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
    date_of_registration = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return f'{self.id} {self.name} {self.email} {self.phone_number} {self.address} {self.date_of_registration}'


class Product(models.Model):
    name_of_product = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    date_of_add = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='product_image',
                              default='default.png',
                              verbose_name='Изображение')

    objects = models.Manager()

    def __str__(self):
        return f'{self.id} {self.name_of_product} {self.description}, {self.price}, {self.quantity}, {self.date_of_add}'


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return f'Заказ {self.pk} клиента - {self.customer}, {self.products}, ст-сть - {self.total_price}'


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name


class Goods(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category,
        on_delete=models.CASCADE)
    description = models.TextField(default='', blank=True)
    price = models.DecimalField(default=999999.99, max_digits=8,
        decimal_places=2)
    quantity = models.PositiveSmallIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(default=5.0, max_digits=3,
    decimal_places=2)


    def __str__(self):
        return self.name