from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class User_Custom(User):
    pass
