from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.utils.timezone import now

class User(AbstractUser, PermissionsMixin):
    
    ADMIN = 1
    STAFF = 1
    EMPLOYEE = 3

    ROLE = (
     (ADMIN, 'Admin'),
     (STAFF, 'Staff'),
     (EMPLOYEE, 'Employee'),
    )

    class Meta:
        verbose_name = 'user',
        verbose_name_plural = 'users'

    fullname = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    role = models.PositiveSmallIntegerField(choices=ROLE, blank=True, null=True, default=3)
    created_at = models.DateField(default=now)
    updated_at = models.DateField(default=now)
    is_active = models.BooleanField(default=True)
    created_by = models.EmailField()
    updated_by = models.EmailField()
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
