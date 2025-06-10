from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    # 추가 필드가 필요하면 여기에 작성

    def __str__(self):
        return self.username 