from django.db import models


from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserAccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone, password=None):
        if not email:
            raise ValueError('Введите корректный e-mail адрес.')
        
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, phone=phone)
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, email, first_name, last_name, phone, password):
        user = self.create_user(email, first_name, last_name, phone, password)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    last_name = models.CharField(max_length=20, blank=True, verbose_name='Фамилия')
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    patronym = models.CharField(max_length=20, blank=True, verbose_name='Отчество')
    email = models.EmailField(max_length=50, unique=True, db_index=True, verbose_name='E-mail')
    photo = models.ImageField(upload_to='photos/%Y-%m-%d/', null=True, blank=True, verbose_name='Фото')
    phone = models.CharField(max_length=20, verbose_name='Телефон', blank=True)
    buy_count = models.PositiveIntegerField(default=0, verbose_name='Количество покупок')
    buy_sum = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, verbose_name='Сумма покупок')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    certificate = models.ImageField(upload_to='certificates/%Y/%m/%d/', blank=True, verbose_name='Сертификат')
    is_certified = models.BooleanField(default=False, verbose_name='Сертифицирован')
    is_active = models.BooleanField(default=True, verbose_name='Аккаунт активен')
    is_staff = models.BooleanField(default=False, verbose_name='Сотрудник')

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def discount_percent(self):
        if 5_000 <= self.buy_sum < 18_000:
            discount = 3
        elif self.buy_sum >= 18_000:
            discount = 5
        else:
            discount = None
        return discount

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ['-register_date']
