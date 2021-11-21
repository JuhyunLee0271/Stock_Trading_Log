# Customized Login User Model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# User를 생성하기 위한 Helper Class(create_user, create_superuser 메서드)
class UserManager(BaseUserManager):
    def create_user(self, name, nickname, email, phone_number, password=None):
        if not name:
            raise ValueError('must have user name')
        if not email:
            raise ValueError('must have user email')
        
        user = self.model(
            name = name,
            email = self.normalize_email(email),
            nickname = nickname,
            phone_number = phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, nickname, email, phone_number, password):
        user = self.create_user(
            name = name,
            nickname = nickname,
            email = self.normalize_email(email),
            phone_number = phone_number,
            password = password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# name, email, nickname, phone_number 필드
class User(AbstractBaseUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    nickname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    # 필수적인 필드(is_active, is_admin)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    # 로그인 시 email, password로 로그인
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'nickname', 'phone_number']

    def __str__(self):
        return self.name

    # 권한 관련 메서드(그냥 true로 줌)
    def has_perm(self, perm, obj=None):
        return True

    # 권한 관련 메서드(그냥 true로 줌)
    def has_module_perms(self, app_label):
        return True

    @property
    # 관리자 계정인지
    def is_staff(self):
        return self.is_admin
